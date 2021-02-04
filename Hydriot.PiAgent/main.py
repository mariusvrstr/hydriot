"""
============================================================
=== This is the main executable file for the application ===
============================================================
"""

from sensors.water_level_sensor_stub import WaterLevelSensor
from sensors.tds_sensor_stub import TDSSensor
from utilities.device import Device
from utilities.config import Config

from abc import ABC, abstractmethod ## abstract module

Device().Boot()

## WaterLevelSensor().StartMonitoring()
TDSSensor().start_monitoring()

