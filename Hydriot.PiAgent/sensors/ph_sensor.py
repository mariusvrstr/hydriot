import sys
import time
import os

from utilities.maths import Math
from sensors.contracts.sensor_base import SensorBase
from drivers.gaohou_pho_14_ph_sensor import GaohouPhSensorDriver
from utilities.app_config import AppConfig

class PhSensorStub(SensorBase):
    def __init__(self):
        SensorBase.__init__(self, None, "pH Sensor", 2, True)        

    def read_implimentation(self):
        ## Stubbed Reading
        reading = Math().random_number(0, 14)
        return reading
    
    def is_available(self): 
        return True

class PhSensor(SensorBase):
    driver = None
    offset = None

    def __init__(self):
        self.driver = GaohouPhSensorDriver()
        SensorBase.__init__(self, self.driver, "pH Sensor", 2, True)
        self.offset = AppConfig().get_ph_offset()

    def convert_raw(self, raw_value):
        # Check manifacturing manual for specific calculation from voltage to PH

        ph_vol = (((raw_value*5.0)/1024)/6)
        ph_value = (3.5 * ph_vol) + self.offset

        return (round(ph_value, 2))