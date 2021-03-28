import sys
import wiringpi as GPIO
import time
import os

from contracts.sensor_abstract import SensorAbstract

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
        reading = -1

        try:
            reading = self._read_implimentation()
        except:
            e = sys.exc_info()[0]
            print(f"Failed to read Water Level Sensor. Error Details >> {e}")
            return False
        finally:
            if reading > -1:
                return True        
        
        return False

    def _read_implimentation(self):
        reading = GPIO.digitalRead(1)
        return reading