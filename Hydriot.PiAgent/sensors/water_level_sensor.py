from contracts.sensor_abstract import SensorAbstract
import wiringpi as GPIO
import time
import os

class WaterLevelSensorStub(SensorAbstract):

    def __init__(self, ):
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
        GPIO.wiringPiSetup()
    
    def is_available(self):
        return True

    def _read_implimentation(self):
        reading = GPIO.digitalRead(1)
        return reading