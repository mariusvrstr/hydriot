from contracts.sensor_abstract import SensorAbstract
from utilities.maths import Math

class TDSSensorStub(SensorAbstract):

    def __init__(self):
        SensorAbstract.__init__(self, "Total Dissolvable Solids (TDS) Sensor", 2)

    def _read_implimentation(self):
        ## Stubbed Reading
        reading = Math().random_number(150, 300)
        return reading
    
    def is_available(self): 
        return True


class TDSSensor(SensorAbstract):

    def __init__(self):
        SensorAbstract.__init__(self, "Total Dissolvable Solids (TDS) Sensor", 2)

    def is_available(self): 
        return False

    def _read_implimentation(self):
        reading = 111
        return reading
