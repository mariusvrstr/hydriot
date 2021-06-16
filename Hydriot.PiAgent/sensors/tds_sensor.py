from utilities.maths import Math
from sensors.contracts.sensor_base import SensorBase
from drivers.cqrobot_total_dissolved_solids_sensor import CQRobotTotalDissolvedSolidsSensorDriver

class TDSSensorStub(SensorBase):

    def __init__(self):
        SensorBase.__init__(self, None, "Total Dissolvable Solids (TDS) Sensor", 2, False, True)

    def read_implimentation(self):
        ## Stubbed Reading
        reading = Math().random_number(150, 300)
        return reading
    
    def is_available(self): 
        return True

class TDSSensor(SensorBase):
    driver = None

    def __init__(self):
        self.driver = CQRobotTotalDissolvedSolidsSensorDriver()
        SensorBase.__init__(self, self.driver, "Total Dissolvable Solids (TDS) Sensor", 2, False, True)


