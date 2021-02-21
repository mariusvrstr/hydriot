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
import asyncio

async def initialize():
    sensors_manager = SensorsManager()
    sensors_manager.register_available()
    sensors_manager.start_monitoring()

    trigger_manager = TriggerManager()
    trigger_manager.register_available()

    device_manager = DeviceManager()
    value = await device_manager.start_device_dashboard(sensors_manager.sensor_list)

def main():     
    asyncio.run(initialize()) 

main()




