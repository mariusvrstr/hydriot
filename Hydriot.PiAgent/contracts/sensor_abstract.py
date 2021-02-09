import time
import os
from datetime import datetime
from abc import ABC, abstractmethod ## abstract module
from utilities.operating_system import OperatingSystem
from utilities.config import Config
import asyncio


class SensorAbstract(ABC):
    _name = "N/A"
    _frequency_in_seconds = 1    
    _is_monitoring = False
    _count = 0

    def __init__(self, sensor_name, reading_frequency):
        self._name = sensor_name    
        self._frequency_in_seconds = reading_frequency
        # must be removed
        self._latest_value = -1
        self._last_read_time = datetime.now()

    def get_last_read_time(self):
        return self._last_read_time
    
    def get_latest_value(self):
        return self._latest_value

    def is_healthy(self): 
        time_passed = (datetime.now() - self._last_read_time).total_seconds()

        if self.is_available and not self._is_monitoring:
            return False
        elif self._is_monitoring and (time_passed > (self._frequency_in_seconds * 3)):
            return False
        else:
            return True
     

    ## IMpliment in the derived class
    def is_available(self): raise NotImplementedError

    def stop_monitoring(self):
        self._is_monitoring = False

    async def start_monitoring(self):
        self._is_monitoring = True

        while self._is_monitoring:
            await asyncio.sleep(self._frequency_in_seconds)
            self.read_value()
        pass
    
    def read_value(self):        
        self._latest_value = self._read_implimentation()
        self._count += 1
        # print(f"{self._count} - Read {self._name} with value of {self._latest_value} - Monitoring: {self._is_monitoring}")    

        self._last_read_time = datetime.now()           

        return self._latest_value


    @abstractmethod
    def _read_implimentation(self):  pass





