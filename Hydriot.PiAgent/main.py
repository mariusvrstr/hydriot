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
import time
import asyncio


async def initialize(sensors_manager, trigger_manager):    
    sensors_manager.register_available()
    sensors_manager.start_monitoring()    
    
    trigger_manager.register_available()
    device_manager = DeviceManager()

    await device_manager.start_device_dashboard(sensors_manager, trigger_manager) 


def main():
    sensors_manager = SensorsManager()
    trigger_manager = TriggerManager()
    
    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(initialize(sensors_manager, trigger_manager))
    except KeyboardInterrupt:
        sensors_manager.cleanup()
        trigger_manager.cleanup()
    # finally:
       # loop.close() # Simulator complains

main()




