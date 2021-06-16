import sys
import time
import os

from drivers.driver_base import DriverBase
from drivers.cqrobot_analog_to_digital_converter import PGA, Channel, ConverterMode, ADS1115
from settings.app_config import AppConfig

## Manufacturer Source
## http://www.baaqii.net/promanage/BU0203%2BBU0481.pdf
## http://www.baaqii.net/promanage/BU0203.zip

class GaohouPhSensorDriver(DriverBase):
    converter_mode = None
    channel = None

    def __init__(self):

        # Set the IIC address (0X48 or 0X49 based on switch on ADC Module)
        self.converter_mode = ConverterMode.x48
        # Set the Programmable Gain Adjustment (Gain and voltage range)
        self.pga = PGA.REG_CONFIG_PGA_6_144V
        # Set the channel
        self.channel = Channel.A1

        DriverBase.__init__(self)        
        pass    

    def initialize(self):
        self.ads1115 = ADS1115()

        self.ads1115.setAddr_ADS1115(self.converter_mode)
        self.ads1115.setGain(self.pga)

    def read_voltage(self):
        ph = self.ads1115.readVoltage(self.channel)
        reading = ph['r']
        return reading

    def read_value(self):
        return self.read_voltage()

    def is_available(self):
        reading = -1
        
        if AppConfig().is_ph_enabled_sensor() is False:
            return False

        try:
            reading = self.read_value()
        except:
            e = sys.exc_info()[0]
            print(f"Failed to read PH. Error Details >> {e}")
            return False
        finally:
            if reading > -1:
                return True        
        
        return False


