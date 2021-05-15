import sys
sys.path.append('../')
import time
import os
from TSL2591 import TSL2591

## Calculate odd and even for visual tic
def NumberType(num):
    if num%2 == 0:
        numtype="even"
    else:
        numtype = "odd"
    return numtype

def PrintHeading(num):
    os.system('clear')
    Heading = "Raspberi Pi - Light Sensor"
    Heading += "[|]" if NumberType(num) == "even" else "[-]"
    print(Heading)
    print("Press Cntr+C in terminal to exit")
    print("")
    return


sensor = TSL2591()

tic=0

try:
    while True:        
        tic += 1

        PrintHeading(tic)

        lux = sensor.Lux
        print('Lux: %d'%lux)
        sensor.TSL2591_SET_LuxInterrupt(50, 200)
        infrared = sensor.Read_Infrared
        print('Infrared light: %d'%infrared)
        visible = sensor.Read_Visible
        print('Visible light: %d'%visible)
        full_spectrum = sensor.Read_FullSpectrum
        print('Full spectrum (IR + visible) light: %d\r\n'%full_spectrum)

        time.sleep(1) 

## Continue with loop until Cntr+C is pressed in terminal
except KeyboardInterrupt:
    print("Exit Monitoring")
    sensor.Disable()
    pass
