from Contracts.sensorAbstract import SensorAbstract

class TDSSensor(SensorAbstract):

    def __init__(self):
        SensorAbstract.__init__(self, "Total Dissolvable Solids (TDS) Sensor")

    def ReadValue(self):
        ## Stubbed Reading
        reading = 145
        return reading
