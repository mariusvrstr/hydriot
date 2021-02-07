"""
============================================================
=== This is the main executable file for the application ===
============================================================
"""

from utilities.config import Config
from utilities.sensors_manager import SensorsManager
from utilities.operating_system import OperatingSystem
import asyncio

## If not present create default config file
Config().initialize_file()

## Scan for available sensors
sensors_manager = SensorsManager()
sensors_manager.register_available()

## Main Problem - The background task loop that should be update the reading are not working
sensors_manager.start_monitoring()

## Display reading updates
sensors_manager.display_sensor_readings_in_console()


