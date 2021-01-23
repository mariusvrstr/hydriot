import wiringpi  as LLS
import time
import os

## Calculate odd and even for visual tic
def NumberType(num):
    if num%2 == 0:
        numtype="even"
    else:
        numtype = "odd"
    return numtype

def PrintHeading(num):
    os.system('clear')
    Heading = "Raspberi Pi - Water Level Sensor "
    Heading += "[|]" if NumberType(num) == "even" else "[-]"
    print(Heading)
    print("Press Cntr+C in terminal to exit")
    print("")
    return

LLS.wiringPiSetup()
tic=0

try:
    while True:        
        tic += 1
        PrintHeading(tic)

        val=LLS.digitalRead(1)
        if val==1:
            print("liquid found!")
        else:
            print("No liquid detected!")

        time.sleep(1) 

## Continue with loop until Cntr+C is pressed in terminal
except KeyboardInterrupt:
    print("Exit Monitoring")
    pass



