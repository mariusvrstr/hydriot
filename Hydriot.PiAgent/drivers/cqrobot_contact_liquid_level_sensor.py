import wiringpi as GPIO
from drivers.driver_base import DriverBase

## Manufacturer Source
## http://www.cqrobot.wiki/index.php/Liquid_Level_Sensor

class CQRobotContactLiquidLevelSensorDriver(DriverBase):

    def __init__(self):
        DriverBase.__init__(self)
        pass    

    def initialize(self):
        GPIO.wiringPiSetup()

    def read_value(self):
        reading = GPIO.digitalRead(1)
        return reading

    def is_available(self):
        reading = -1

        try:
            # TODO: If there is nothing it still reads as 0 need better mechanism
            reading = self.read_value()
        except:
            e = sys.exc_info()[0]
            print(f"Failed to read Liquid Level Sensor. Error Details >> {e}")
            return False
        finally:
            if reading > -1:
                return True        
        
        return False