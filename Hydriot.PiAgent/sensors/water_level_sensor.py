import sys
import wiringpi as GPIO
import time
import os

from sensors.sensor_base import SensorBase

class WaterLevelSensorStub(SensorBase):

    def __init__(self, ):
        SensorBase.__init__(self, "Water Level Sensor", 1)

    def _read_implimentation(self):
        ## Stubbed Reading
        reading = 1
        return reading
    
    def is_available(self):
        return True

class WaterLevelSensor(SensorBase):

    def __init__(self):
        SensorBase.__init__(self, "Water Level Sensor", 1)
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