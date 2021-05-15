import sys
sys.path.append('../')
import time
import os
from ADS1115 import ADS1115

## Calculate odd and even for visual tic
def NumberType(num):
    if num%2 == 0:
        numtype="even"
    else:
        numtype = "odd"
    return numtype

def PrintHeading(num):
    os.system('clear')
    Heading = "Raspberi Pi - TDS Sensor"
    Heading += "[|]" if NumberType(num) == "even" else "[-]"
    print(Heading)
    print("Press Cntr+C in terminal to exit")
    print("")
    return

ADS1115_REG_CONFIG_PGA_6_144V        = 0x00 # 6.144V range = Gain 2/3
ADS1115_REG_CONFIG_PGA_4_096V        = 0x02 # 4.096V range = Gain 1
ADS1115_REG_CONFIG_PGA_2_048V        = 0x04 # 2.048V range = Gain 2 (default)
ADS1115_REG_CONFIG_PGA_1_024V        = 0x06 # 1.024V range = Gain 4
ADS1115_REG_CONFIG_PGA_0_512V        = 0x08 # 0.512V range = Gain 8
ADS1115_REG_CONFIG_PGA_0_256V        = 0x0A # 0.256V range = Gain 16
ads1115 = ADS1115()

tic=0

try:
    while True:        
        tic += 1

        #Set the IIC address (0X48 or 0X49 based on switch on ADC Module)
        ads1115.setAddr_ADS1115(0x48)
        #Sets the gain and input voltage range.
        ads1115.setGain(ADS1115_REG_CONFIG_PGA_6_144V)
        #Get the Digital Value of Analog of selected channel (4 Channels on ADC Module: 0 to 3)
        adc1 = ads1115.readVoltage(2)
        # Clear previous values and set heading

        tds = ads1115.readValue()

        PrintHeading(tic)

        print("Voltage: A1:%dmV "%(adc1['r']))
        print("TDS Value: %d"%(tds['r']))

        time.sleep(1) 

## Continue with loop until Cntr+C is pressed in terminal
except KeyboardInterrupt:
    print("Exit Monitoring")
    pass
