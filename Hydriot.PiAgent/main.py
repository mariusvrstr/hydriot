"""
============================================================
=== This is the main executable file for the application ===
============================================================
"""

from utilities.config import Config
from utilities.sensors import Sensors
from utilities.operating_system import OperatingSystem

## If not present create default config file
Config().initialize_file()

## Scan for available sensors
Sensors().RegisterAvailable()
