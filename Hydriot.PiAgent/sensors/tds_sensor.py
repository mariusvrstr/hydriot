from contracts.sensor_abstract import SensorAbstract
from utilities.maths import Math
import time
import os
from sensors.resources.CQRobot_ADS1115 import ADS1115

class TDSSensorStub(SensorAbstract):

    def __init__(self):
        SensorAbstract.__init__(self, "Total Dissolvable Solids (TDS) Sensor", 2)

    def _read_implimentation(self):
        ## Stubbed Reading
        reading = Math().random_number(150, 300)
        return reading
    
    def is_available(self): 
        return True


class TDSSensor(SensorAbstract):

    def __init__(self):
        SensorAbstract.__init__(self, "Total Dissolvable Solids (TDS) Sensor", 2)

        self.ADS1115_REG_CONFIG_PGA_6_144V        = 0x00 # 6.144V range = Gain 2/3
        self.ADS1115_REG_CONFIG_PGA_4_096V        = 0x02 # 4.096V range = Gain 1
        self.ADS1115_REG_CONFIG_PGA_2_048V        = 0x04 # 2.048V range = Gain 2 (default)
        self.ADS1115_REG_CONFIG_PGA_1_024V        = 0x06 # 1.024V range = Gain 4
        self.ADS1115_REG_CONFIG_PGA_0_512V        = 0x08 # 0.512V range = Gain 8
        self.ADS1115_REG_CONFIG_PGA_0_256V        = 0x0A # 0.256V range = Gain 16
        self.ads1115 = ADS1115()

    def is_available(self): 
        reading = -1

        try:
            reading = self._read_implimentation()
        except:
            return False
                
        if reading > -1:
            return True
        
        return False

    def _read_implimentation(self):

         #Set the IIC address (0X48 or 0X49 based on switch on ADC Module)
        self.ads1115.setAddr_ADS1115(0x48)

        #Sets the gain and input voltage range.
        self.ads1115.setGain(self.ADS1115_REG_CONFIG_PGA_6_144V)

        #Get the Digital Value of Analog of selected channel (4 Channels on ADC Module: 0 to 3)
        adc1 = self.ads1115.readVoltage(2)
        # Clear previous values and set heading

        tds = self.ads1115.readValue()
        reading = tds['r']

        return reading
