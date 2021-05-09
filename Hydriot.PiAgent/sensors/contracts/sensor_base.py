from common.sensor_summary import SensorSummary
from common.scheduling_abstract import SchedulingAbstract
from abc import ABC, abstractmethod ## abstract module
import sys
import asyncio
import time

class SensorBase(SchedulingAbstract):    
    sensor_summary = None
    driver = None

    def __init__(self, driver, sensor_name, frequency_in_seconds, use_average, expect_deviation):
        self.driver = driver
        self.sensor_summary = SensorSummary(sensor_name, frequency_in_seconds, expect_deviation)
        SchedulingAbstract.__init__(self, frequency_in_seconds, sensor_name, use_average)

    def get_last_read_time(self):
        return self.sensor_summary.last_execution
    
    def get_latest_value(self):
        return self.sensor_summary.current_value

    def convert_raw(self, raw_value):
        return raw_value

    async def read_average(self, count, delay_in_milliseconds):
        total = 0        

        for i in range(count):
            value = self.read_raw()
            total += value
            if delay_in_milliseconds > 0:
                await asyncio.sleep(delay_in_milliseconds/1000)          

        average = total / count
        converted = self.convert_raw(average)
        self.sensor_summary.update_value(converted)
       
        return converted


    def read_value(self):
        value = self.read_raw()
        converted = self.convert_raw(value)
        self.sensor_summary.update_value(converted)
        return converted

    def read_raw(self):
        if self.driver is None:
            raise NotImplementedError

        try:
            value = self.driver.read_value()

            return value
        except:
            e = sys.exc_info()[0]
            print(f"Failed to read [{self.sensor_summary.name}]. Error Details >> {e}")
            self.sensor_summary.set_last_read_error()            
            return None

    def is_available(self):
        if self.driver is None:
            raise NotImplementedError
        
        try:
            return self.driver.is_available()
        except:
            e = sys.exc_info()[0]
            print(f"Failed to verify if [{self.sensor_summary.name}] is available. Error Details >> {e}")
            self.sensor_summary.set_last_read_error()
            return False

        pass

