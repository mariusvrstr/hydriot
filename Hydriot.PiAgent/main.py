"""
============================================================
=== This is the main executable file for the application ===
============================================================
"""

from utilities.config import Config
from utilities.trigger_manager import TriggerManager
from utilities.operating_system import OperatingSystem
from utilities.device_manager import DeviceManager
from utilities.integration_adapter import IntegrationAdapter
from hydriot import Hydriot
from utilities.dependency_injection import Container

import time
import asyncio

class Main():
    hydriot = None

    def __init__(self):
        self.hydriot = Hydriot()    

    async def boot(self, trigger_manager, integration_adapter):
        container = Container()

        tds_sensor =  container.tds_factory()

        if tds_sensor.is_available():
            self.hydriot.set_tds_sensor(tds_sensor.sensor_summary)
            asyncio.ensure_future(tds_sensor.start_monitoring())

        water_level_sensor =  container.water_level_sensor_factory()
            
        if water_level_sensor.is_available():
            self.hydriot.set_water_level_sensor(water_level_sensor.sensor_summary)
            asyncio.ensure_future(water_level_sensor.start_monitoring())
    
        trigger_manager.register_available()
        device_manager = DeviceManager()

        # integration_adapter.start_monitoring(sensor_manager.sensor_list)

        await device_manager.start_device_dashboard(self.hydriot, trigger_manager, integration_adapter)

    def start(self):
        #sensors_manager = SensorsManager()
        trigger_manager = TriggerManager()
        integration_adapter = IntegrationAdapter(30)
        
        loop = asyncio.get_event_loop()

        try:
            loop.run_until_complete(self.boot(trigger_manager, integration_adapter))
        
        except KeyboardInterrupt:
            hydriot.tds_sensor
            sensors_manager.cleanup()
            trigger_manager.cleanup()
            integration_adapter.cleanup()
        # finally:
        # loop.close() # Simulator complains


Main().start()




