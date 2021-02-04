"""
============================================================
=== This is the main executable file for the application ===
============================================================
"""

from sensors.water_level_sensor_stub import WaterLevelSensor
from sensors.tds_sensor_stub import TDSSensor

from abc import ABC, abstractmethod ## abstract module

## WaterLevelSensor().StartMonitoring()
TDSSensor().start_monitoring()

