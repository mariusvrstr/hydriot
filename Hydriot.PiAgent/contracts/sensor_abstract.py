from datetime import datetime
from abc import ABC, abstractmethod
from utilities.operating_system import OperatingSystem
from utilities.config import Config
from contracts.sensor_summary import SensorSummary

import time
import os
import asyncio

class SensorAbstract(ABC):
    _frequency_in_seconds = 1
    _is_monitoring = False
    sensor_summary = None    

    def __init__(self, sensor_name, frequency):
        self._frequency_in_seconds = frequency
        self.sensor_summary = SensorSummary(sensor_name, frequency)

    def get_last_read_time(self):
        return self.sensor_summary.last_execution
    
    def get_latest_value(self):
        return self.sensor_summary.current_value

    def stop_monitoring(self):
        self._is_monitoring = False

    async def start_monitoring(self):
        self._is_monitoring = True

        while self._is_monitoring:
            self.read_value()
            await asyncio.sleep(self._frequency_in_seconds)            
        pass
    
    def read_value(self):
        value = self._read_implimentation()
        self.sensor_summary.update_value(value)
        return value

    @abstractmethod
    def _read_implimentation(self): raise NotImplementedError

    @abstractmethod
    def is_available(self): raise NotImplementedError


