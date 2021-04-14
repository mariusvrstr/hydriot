from datetime import datetime
from abc import ABC, abstractmethod
from utilities.operating_system import OperatingSystem
from utilities.config import Config
from contracts.sensor_summary import SensorSummary
from contracts.scheduling_abstract import SchedulingAbstract

import time
import os
import asyncio

class SensorBase(SchedulingAbstract):    
    sensor_summary = None    

    def __init__(self, sensor_name, frequency_in_seconds):
        self.sensor_summary = SensorSummary(sensor_name, frequency_in_seconds)
        SchedulingAbstract.__init__(self, frequency_in_seconds)

    def get_last_read_time(self):
        return self.sensor_summary.last_execution
    
    def get_latest_value(self):
        return self.sensor_summary.current_value

    def read_value(self):
        value = self._read_implimentation()
        self.sensor_summary.update_value(value)
        return value

    @abstractmethod
    def _read_implimentation(self): raise NotImplementedError

    @abstractmethod
    def is_available(self): raise NotImplementedError


