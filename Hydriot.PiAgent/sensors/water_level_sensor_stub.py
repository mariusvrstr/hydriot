from contracts.sensor_abstract import SensorAbstract

class WaterLevelSensor(SensorAbstract):

    def __init__(self):
        SensorAbstract.__init__(self, "Water Level Sensor")

    def read_value(self):
        ## Stubbed Reading
        reading = 1
        return reading
