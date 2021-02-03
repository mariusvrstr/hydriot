import time
import os
from abc import ABC, abstractmethod ## abstract module

class SensorAbstract(ABC):
    Name = "N/A"
    FrequencyInSeconds = 1

    def __init__(self, sensorName):
        self.Name = sensorName

    ##TODO: Missing functionality
    def IsHealthy(self): raise NotImplementedError 

    ##TODO: Missing functionality
    def IsAvailable(self): raise NotImplementedError

    def SetFrequency(self, inSeconds):
        self.FrequencyInSeconds = inSeconds
        pass     

    def StartMonitoring(self):
        tic=0        

        try:
            while True: 
                tic += 1
                currentValue = self.ReadValue()

                ## Make OS Resilient (Clear vs CLS)
                os.system('cls')

                header = "Raspberry Pi - "
                header += self.Name
                print(header)
                print("=======================================================")

                print("Current Value: " + str(currentValue))

                print("")
                footer = "...Press Cntr+C to exit monitoring "
                if tic%2 == 0: footer += "[|]"
                else: footer += "[-]"
                print(footer)

                time.sleep(self.FrequencyInSeconds) 
                
        except KeyboardInterrupt:
            print("Exit Monitoring")
            pass
        pass

    @abstractmethod
    def ReadValue(self):  pass





