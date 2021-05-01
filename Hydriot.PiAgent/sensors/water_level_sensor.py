import sys
import time
import os

from utilities.pin_converter import GPIO
from sensors.sensor_base import SensorBase
from drivers.cqrobot_contact_liquid_level_sensor import CQRobotContactLiquidLevelSensorDriver

class WaterLevelSensorStub(SensorBase):

    def __init__(self, ):
        SensorBase.__init__(self, None, "Water Level Sensor", 1, False)

    def read_implimentation(self): # override driver default
        return 1  ## Stubbed Reading
    
    def is_available(self): # override driver default
        return True

class WaterLevelSensor(SensorBase):
    driver = None

    def __init__(self):
        # TODO: Move this to DI configuration
        self.driver = CQRobotContactLiquidLevelSensorDriver(GPIO.GPIO018)
        SensorBase.__init__(self, self.driver, "Water Level Sensor", 1, False)



        