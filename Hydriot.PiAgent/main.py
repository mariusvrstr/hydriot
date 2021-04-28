"""
============================================================
=== This is the main executable file for the application ===
============================================================
"""

from utilities.app_config import AppConfig
from utilities.console_manager import ConsoleManager
from utilities.integration_adapter import IntegrationAdapter
from hydriot import Hydriot
from utilities.dependency_injection import Container
import RPi.GPIO as GPIO

import time
import asyncio
import os

class Main():
    hydriot = None
    tds_sensor = None
    water_level_sensor = None
    
    light_trigger = None
    water_pump_trigger = None

    def __init__(self):
        self.hydriot = Hydriot()    

    async def boot(self, integration_adapter):
        container = Container()

        self.ph_sensor = container.ph_sensor_factory()
        
        if self.ph_sensor.is_available():
            self.hydriot.set_ph_sensor(self.ph_sensor.sensor_summary)
            asyncio.ensure_future(self.ph_sensor.run_schedule())

        self.tds_sensor =  container.tds_factory()

        if self.tds_sensor.is_available():
            self.hydriot.set_tds_sensor(self.tds_sensor.sensor_summary)
            asyncio.ensure_future(self.tds_sensor.run_schedule())

        self.water_level_sensor =  container.water_level_sensor_factory()
            
        if self.water_level_sensor.is_available():
            self.hydriot.set_water_level_sensor(self.water_level_sensor.sensor_summary)
            asyncio.ensure_future(self.water_level_sensor.run_schedule())

        self.light_trigger = container.light_relay_factory()
        
        if self.light_trigger._is_enabled:
            self.hydriot.set_light_trigger(self.light_trigger)

        self.water_pump_trigger = container.pump_relay_factory()
        
        if self.water_pump_trigger._is_enabled:
            self.hydriot.set_water_pump_trigger(self.water_pump_trigger)
    
        console_manager = ConsoleManager()

        # integration_adapter.start_monitoring(sensor_manager.sensor_list)

        await console_manager.start_device_dashboard(self.hydriot, integration_adapter)

    def start(self):
        integration_adapter = IntegrationAdapter(30)
        
        loop = asyncio.get_event_loop()

        try:
            loop.run_until_complete(self.boot(integration_adapter))
        
        except KeyboardInterrupt:
            ConsoleManager().clear_console()

            self.tds_sensor.stop_schedule()
            self.water_level_sensor.stop_schedule()
            self.ph_sensor.stop_schedule()

            if AppConfig().get_enable_sim() == False:
                GPIO.cleanup()

            integration_adapter.cleanup()
            # TODO: asynco wait to exit loops
            time.sleep(10) 

Main().start()
ConsoleManager().clear_console()


