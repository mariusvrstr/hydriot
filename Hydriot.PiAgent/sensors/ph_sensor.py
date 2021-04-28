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

    def __init__(self):
        self.driver = GaohouPhSensorDriver()
        SensorBase.__init__(self, self.driver, "pH Sensor", 2)
