"""
============================================================
=== This is the main executable file for the application ===
============================================================
"""

from utilities.config import Config
from utilities.trigger_manager import TriggerManager
from utilities.sensors_manager import SensorsManager
from utilities.operating_system import OperatingSystem
from utilities.device_manager import DeviceManager
from utilities.integration_adapter import IntegrationAdapter
import time
import asyncio


async def initialize(sensor_manager, trigger_manager, integration_adapter):    
    sensor_manager.register_available()
    sensor_manager.start_monitoring()    
    
    trigger_manager.register_available()
    device_manager = DeviceManager()

    integration_adapter.start_monitoring(sensor_manager.sensor_list)

    await device_manager.start_device_dashboard(sensor_manager, trigger_manager, integration_adapter) 


def main():
    sensors_manager = SensorsManager()
    trigger_manager = TriggerManager()
    integration_adapter = IntegrationAdapter(30)
    
    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(initialize(sensors_manager, trigger_manager, integration_adapter))
    
    except KeyboardInterrupt:
        sensors_manager.cleanup()
        trigger_manager.cleanup()
        integration_adapter.cleanup()
    # finally:
       # loop.close() # Simulator complains

main()




