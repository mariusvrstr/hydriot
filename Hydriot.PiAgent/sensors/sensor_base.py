from common.sensor_summary import SensorSummary
from common.scheduling_abstract import SchedulingAbstract
from abc import ABC, abstractmethod ## abstract module

class SensorBase(SchedulingAbstract):    
    sensor_summary = None
    driver = None  

    def __init__(self, driver, sensor_name, frequency_in_seconds):
        self.driver = driver
        self.sensor_summary = SensorSummary(sensor_name, frequency_in_seconds)
        SchedulingAbstract.__init__(self, frequency_in_seconds, sensor_name)

    def get_last_read_time(self):
        return self.sensor_summary.last_execution
    
    def get_latest_value(self):
        return self.sensor_summary.current_value

    def convert_raw(self, raw_value):
        return raw_value

    def read_average(self):
        raise NotImplementedError  
        pass

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
            return False

    def is_available(self):
        if self.driver is None:
            raise NotImplementedError
        
        try:
            return self.driver.is_available()
        except:
            e = sys.exc_info()[0]
            print(f"Failed to verify if [{self.sensor_summary.name}] is available. Error Details >> {e}")
            return False

        pass

