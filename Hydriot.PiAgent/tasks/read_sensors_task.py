import asyncio
import RPi.GPIO as GPIO
import time

from tasks.contracts.base_task import BaseTask
from settings.app_config import AppConfig
from utilities.dependency_injection import Container
from utilities.console_manager import ConsoleManager
from utilities.integration_adapter import IntegrationAdapter
from common.task_manager import TaskManager
from hydriot import Hydriot, SensorType, TriggerType
from common.sensor_summary import SensorSummary
from PyQt5.QtCore import pyqtSignal

class ReadSensorsTask(BaseTask):
    integration_adapter = None
    hydriot = None
    task_manager = None
    progress = pyqtSignal(SensorSummary)    

    def cleanup(self):
        self.tds_sensor.stop_schedule()
        self.water_level_sensor.stop_schedule()
        self.ph_sensor.stop_schedule()
        self.voltage_tester.stop_schedule()

        if AppConfig().get_enable_sim() == False:
            GPIO.cleanup()

        self.integration_adapter.cleanup()

        time.sleep(5) 

    async def run_container(self):
        console_manager = ConsoleManager()

        while self.task_manager.is_working():
            console_manager.display_sensors(self.hydriot, self.integration_adapter, self.task_manager)

            ## Update pump status from water level sensor
            if (self.hydriot.water_pump_trigger is not None):
                self.hydriot.water_pump_trigger.sync_status()

            if (self.hydriot.tds_sensor is not None):
                self.progress.emit(self.hydriot.tds_sensor)
            
            if (self.hydriot.ph_sensor is not None):
                self.progress.emit(self.hydriot.ph_sensor)

            if (self.hydriot.voltage_sensor is not None):  
                self.progress.emit(self.hydriot.voltage_sensor)

            if (self.hydriot.water_level_sensor is not None):  
                self.progress.emit(self.hydriot.water_level_sensor)   

            await asyncio.sleep(3)
    
    def register_sensor(self, sensor_type, sensor):
        if sensor.is_enabled and sensor.is_available():            
            asyncio.ensure_future(sensor.run_schedule(self.task_manager))
            self.hydriot.set_sensor(sensor_type, sensor.sensor_summary)

    def register_trigger(self, trigger_type, trigger, dependant_sensor = None):         
        if dependant_sensor is not None:
            trigger.set_dependant_sensor_summary(dependant_sensor.sensor_summary)

        if trigger.is_enabled:            
            self.hydriot.set_trigger(trigger_type, trigger)

    async def run_all(self):
        self.task_manager = TaskManager()
        container = Container()

        ph_sensor = container.ph_sensor_factory()
        self.register_sensor(SensorType.Ph, ph_sensor)

        tds_sensor = container.tds_factory()
        self.register_sensor(SensorType.TDS, tds_sensor)

        water_level_sensor = container.water_level_sensor_factory()
        self.register_sensor(SensorType.WaterLevel, water_level_sensor)

        voltage_sensor = container.voltage_tester_factory()
        self.register_sensor(SensorType.Voltage, voltage_sensor)

        ## self.register_sensor(container.light_sensor_infrared_factory())

        self.register_trigger(TriggerType.NutrientDose, container.nutrient_relay_factory(), tds_sensor)
        self.register_trigger(TriggerType.PhDose,container.ph_down_relay_factory())
        self.register_trigger(TriggerType.WaterPumpCutout,container.water_pump_relay_factory(), water_level_sensor)

        self.integration_adapter = IntegrationAdapter(30)

        await self.run_container()
    
    def run_custom(self):
        print(f"starting sensors reading")

        self.hydriot = Hydriot()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop) 

        try:            
            loop.run_until_complete(self.run_all())
        
        except KeyboardInterrupt:
            print (f'stopped')
        
        ## self.cleanup()
        self.finished.emit()

