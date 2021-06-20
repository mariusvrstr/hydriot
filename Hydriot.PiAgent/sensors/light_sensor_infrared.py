import sys

from utilities.maths import Math
from sensors.contracts.sensor_base import SensorBase
from drivers.cqrobot_light_sensor import CQRobotLightSensor
from settings.app_config import AppConfig

class LightSensorInfraredStub(SensorBase):
    def __init__(self):
        enabled = AppConfig().is_light_enabled_sensor()
        SensorBase.__init__(self, None, "Light Sensor", 2, enabled, True)        

    def read_implimentation(self):
        ## Stubbed Reading
        reading = Math().random_number(0, 100)
        return reading
    
    def is_available(self): 
        return True

class LightSensorInfrared(SensorBase):
    driver = None

    def __init__(self):
        enabled = AppConfig().is_light_enabled_sensor()
        self.driver = CQRobotLightSensor()
        SensorBase.__init__(self, self.driver, "Light Sensor", 2, enabled, True)
        self.sensor_summary.define_health_parameters(True)

    def read_raw(self):
        if self.driver is None:
            raise NotImplementedError

        try:
            value = self.driver.read_infrared()

            return value
        except:
            e = sys.exc_info()[0]
            print(f"Failed to read [{self.sensor_summary.name}]. Error Details >> {e}")
            self.sensor_summary.set_last_read_error()            
            return None
