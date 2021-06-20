import time
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSignal
from time import sleep
from hydriot import Hydriot
from utilities.dependency_injection import Container
from settings.app_config import AppConfig
from utilities.console_manager import ConsoleManager
from utilities.integration_adapter import IntegrationAdapter
from common.sensor_summary import SensorSummary

# from contracts.counter import Counter
import asyncio
import RPi.GPIO as GPIO

class BackgroundWorker(QObject):
    finished = pyqtSignal()
    enabled = False
    integration_adapter = None
    hydriot = None
    progress = pyqtSignal(SensorSummary)    

    async def run_all(self):
        self.enabled = True
        container = Container()

        self.ph_sensor = container.ph_sensor_factory()
        
        if self.ph_sensor.is_enabled and self.ph_sensor.is_available():
            self.hydriot.set_ph_sensor(self.ph_sensor.sensor_summary)
            asyncio.ensure_future(self.ph_sensor.run_schedule())

        self.tds_sensor =  container.tds_factory()

        if self.tds_sensor.is_enabled and self.tds_sensor.is_available():
            self.hydriot.set_tds_sensor(self.tds_sensor.sensor_summary)
            asyncio.ensure_future(self.tds_sensor.run_schedule())

        self.water_level_sensor =  container.water_level_sensor_factory()
            
        if self.water_level_sensor.is_enabled and self.water_level_sensor.is_available():
            self.hydriot.set_water_level_sensor(self.water_level_sensor.sensor_summary)
            asyncio.ensure_future(self.water_level_sensor.run_schedule())

        self.voltage_tester = container.voltage_tester_factory()
        if self.voltage_tester.is_enabled and self.voltage_tester.is_available():
            self.hydriot.set_voltage_tester(self.voltage_tester.sensor_summary)
            asyncio.ensure_future(self.voltage_tester.run_schedule())

        # TODO: Need to get this working
        # self.light_sensor_infrared =  container.light_sensor_infrared_factory()

        # if self.light_sensor_infrared.is_available():
           # self.hydriot.set_light_sensor_infrared(self.light_sensor_infrared.sensor_summary)
           # asyncio.ensure_future(self.light_sensor_infrared.run_schedule())

        self.nutrient_disposer_trigger = container.nutrient_relay_factory() 
        if self.nutrient_disposer_trigger.is_enabled:
            self.hydriot.set_nutrient_disposer_trigger(self.nutrient_disposer_trigger)

        self.ph_down_trigger = container.ph_down_relay_factory()      
        if self.ph_down_trigger.is_enabled:
            self.hydriot.set_ph_down_trigger(self.ph_down_trigger)

        self.water_pump_trigger = container.water_pump_relay_factory()      
        if self.water_pump_trigger.is_enabled:
            self.hydriot.set_water_pump_trigger(self.water_pump_trigger)

        self.integration_adapter = IntegrationAdapter(30)

        console_manager = ConsoleManager()

        while True:            
            console_manager.display_sensors(self.hydriot, self.integration_adapter)

            self.progress.emit(self.hydriot.tds_sensor)
            self.progress.emit(self.hydriot.ph_sensor)
            self.progress.emit(self.hydriot.voltage_tester)
            self.progress.emit(self.hydriot.water_level_sensor)   

            await asyncio.sleep(2)


    def cleanup(self):
        self.tds_sensor.stop_schedule()
        self.water_level_sensor.stop_schedule()
        self.ph_sensor.stop_schedule()
        self.voltage_tester.stop_schedule()

        if AppConfig().get_enable_sim() == False:
            GPIO.cleanup()

        self.integration_adapter.cleanup()
        # TODO: asynco wait to exit loops
        time.sleep(10) 

    def run(self): 
        self.hydriot = Hydriot()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        try:            
            loop.run_until_complete(self.run_all())
        
        except KeyboardInterrupt:
            print (f'stopped')
        
        self.cleanup()
        self.finished.emit()