from utilities.maths import Math
from sensors.contracts.sensor_base import SensorBase
from drivers.rasbee_voltage_tester import RasbeeVoltageTesterDriver
from settings.app_config import AppConfig

class VoltageTesterStub(SensorBase):

    def __init__(self):
        enabled = AppConfig().is_voltage_tester_enabled()
        SensorBase.__init__(self, None, "Battery Voltage Tester", 2, enabled, False)

    def read_implimentation(self):
        ## Stubbed Reading
        reading = Math().random_number(0, 12)
        return reading
    
    def is_available(self): 
        return True

class VoltageTester(SensorBase):
    driver = None

    def convert_raw(self, raw_value):
        converter = raw_value / 199
        
        return round(converter, 2)

    def __init__(self):
        enabled = AppConfig().is_voltage_tester_enabled()
        self.driver = RasbeeVoltageTesterDriver()
        SensorBase.__init__(self, self.driver, "Battery Voltage Tester", 2, enabled, False)
        self.sensor_summary.define_health_parameters(True, 10, 14)


