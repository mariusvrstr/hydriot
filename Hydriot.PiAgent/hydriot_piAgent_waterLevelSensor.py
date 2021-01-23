from hydriot_piAgent_contracts import SensorAbstract

class WaterLevelSensor(SensorAbstract):

    def __init__(self):
        SensorAbstract.__init__(self, "Water Level Sensor")

    def ReadValue(self):
        ## Stubbed Reading
        reading = 1
        return reading
