from contracts.sensor_abstract import SensorAbstract

class WaterLevelSensorStub(SensorAbstract):

    def __init__(self):
        SensorAbstract.__init__(self, "Water Level Sensor", 1)

    def _read_implimentation(self):
        ## Stubbed Reading
        reading = 1
        return reading
    
    def is_available(self):
        return True


class WaterLevelSensor(SensorAbstract):

    def __init__(self):
        SensorAbstract.__init__(self, "Water Level Sensor", 1)
    
    def is_available(self):
        return False

    async def _read_implimentation(self):
        reading = 0
        return reading