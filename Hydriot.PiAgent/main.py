"""
============================================================
=== This is the main executable file for the application ===
============================================================
"""

from utilities.config import Config
from utilities.sensors_manager import SensorsManager
from utilities.operating_system import OperatingSystem
import concurrent.futures
import asyncio


async def start_sensors():
    ## Scan for available sensors
    sensors_manager = SensorsManager()
    sensors_manager.register_available()
    sensors_manager.start_monitoring()

    value = await sensors_manager.monitor_sensors()

def main():     
    asyncio.run(start_sensors()) 

main()




