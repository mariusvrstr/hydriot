import sys
sys.path.append('../')
import time
import os
from CQRobot_ADS1115 import PGA, Channel, ConverterMode, ADS1115

## Calculate odd and even for visual tic
def NumberType(num):
    if num%2 == 0:
        numtype="even"
    else:
        numtype = "odd"
    return numtype

def PrintHeading(num):
    os.system('clear')
    Heading = "Raspberi Pi - pH Sensor"
    Heading += "[|]" if NumberType(num) == "even" else "[-]"
    print(Heading)
    print("Press Cntr+C in terminal to exit")
    print("")
    pass


class PhSensor():
    ads1115 = None

    def __init__(self):
        self.ads1115 = ADS1115()

        #Set the IIC address (0X48 or 0X49 based on switch on ADC Module)
        self.ads1115.setAddr_ADS1115(ConverterMode.x48)

        #Sets the gain and input voltage range.
        self.ads1115.setGain(PGA.REG_CONFIG_PGA_6_144V)

    def read_raw(self):        

        #Get the Digital Value of Analog of selected channel (4 Channels on ADC Module: 0 to 3)
        ph = self.ads1115.readVoltage(Channel.A1) ## Channel A1
        reading = ph['r']

        return reading

    def convert_raw(self, raw_value):
            # Check manifacturing manual for specific calculation from voltage to PH
            offset = -4.21 ## Calibrated against pH 7 from shorted BNC

            ph_vol = (((raw_value*5.0)/1024)/6)
            ph_value = (3.5 * ph_vol) + offset

            new_value = round(ph_value, 2)

            return new_value

    def read_average(self, count, delay_in_milliseconds):
        total = 0        

        for i in range(count):
            value = self.read_raw()
            total += value
            if delay_in_milliseconds > 0:
                time.sleep(delay_in_milliseconds/1000)    

        average = total / count
        converted = self.convert_raw(average)

        return converted


sensor = PhSensor()

tic=0

try:
    while True:        
        tic += 1
        value = sensor.read_average(20, 10)

        PrintHeading(tic)
        print(f"Ph Value: {value}")

        time.sleep(1) 

## Continue with loop until Cntr+C is pressed in terminal
except KeyboardInterrupt:
    print("Exit Monitoring")
    pass
