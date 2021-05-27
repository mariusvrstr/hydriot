import sys
import time
import os

from utilities.maths import Math
from sensors.contracts.sensor_base import SensorBase
from drivers.rasbee_voltage_tester import RasbeeVoltageTesterDriver

class VoltageTesterStub(SensorBase):

    def __init__(self):
        SensorBase.__init__(self, None, "Battery Voltage Tester", 2, False, False)

    def read_implimentation(self):
        ## Stubbed Reading
        reading = Math().random_number(0, 12)
        return reading
    
    def is_available(self): 
        return True

class VoltageTester(SensorBase):
    driver = None

    def convert_raw(self, raw_value):
        converter = raw_value / 220

        return converter

    def __init__(self):
        self.driver = RasbeeVoltageTesterDriver()
        SensorBase.__init__(self, self.driver, "Battery Voltage Tester", 2, False, True)


