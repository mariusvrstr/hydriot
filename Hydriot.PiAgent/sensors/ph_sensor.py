import sys
import time
import os

from utilities.maths import Math
from sensors.sensor_base import SensorBase
from drivers.gaohou_pho_14_ph_sensor import GaohouPhSensorDriver

class PhSensorStub(SensorBase):

    def __init__(self):
        SensorBase.__init__(self, None, "pH Sensor", 2)

    def read_implimentation(self):
        ## Stubbed Reading
        reading = Math().random_number(150, 300)
        return reading
    
    def is_available(self): 
        return True

class PhSensor(SensorBase):
    driver = None
    calibration = 0

    def __init__(self):
        self.driver = GaohouPhSensorDriver()
        SensorBase.__init__(self, self.driver, "pH Sensor", 2)

    def convert_raw(self, raw_value):
        ## Example 1
        # ph_vol = raw_value*5.0/1024/6
        # ph_value = -5.70 * ph_vol + self.calibration 

        ph_vol = raw_value*5.0/1024
        ph_value = ph_vol - 5.70

        return (round(ph_value, 2))