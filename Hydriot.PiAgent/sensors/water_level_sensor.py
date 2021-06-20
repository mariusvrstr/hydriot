from utilities.pin_converter import GPIO
from sensors.contracts.sensor_base import SensorBase
from drivers.cqrobot_contact_liquid_level_sensor import CQRobotContactLiquidLevelSensorDriver
from settings.app_config import AppConfig

class WaterLevelSensorStub(SensorBase):

    def __init__(self, ):
        enabled = AppConfig().is_water_level_sensor_enabled()
        SensorBase.__init__(self, None, "Water Level Sensor", 1, enabled, False)

    def read_implimentation(self): # override driver default
        return 1  ## Stubbed Reading
    
    def is_available(self): # override driver default
        return True

class WaterLevelSensor(SensorBase):
    driver = None

    def __init__(self):
        enabled = AppConfig().is_water_level_sensor_enabled()
        self.driver = CQRobotContactLiquidLevelSensorDriver(GPIO.GPIO018)
        SensorBase.__init__(self, self.driver, "Water Level Sensor", 1, enabled, False)
        self.sensor_summary.define_health_parameters(False, 0, 1)



        