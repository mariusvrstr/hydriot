from contracts.sensor_abstract import SensorAbstract

class WaterLevelSensorStub(SensorAbstract):

    def __init__(self):
        SensorAbstract.__init__(self, "Water Level Sensor")

    def read_value(self):
        ## Stubbed Reading
        reading = 1
        return reading
    
    def is_healthy(self):
        return False


class WaterLevelSensor(SensorAbstract):

    def __init__(self):
        SensorAbstract.__init__(self, "Water Level Sensor")

    def read_value(self):
        reading = 0
        return reading