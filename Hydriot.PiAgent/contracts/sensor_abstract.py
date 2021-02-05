import time
import os
from abc import ABC, abstractmethod ## abstract module
from utilities.operating_system import OperatingSystem
from utilities.config import Config

class SensorAbstract(ABC):
    _name = "N/A"
    _frequency_in_seconds = 1

    def __init__(self, sensor_name):
        self._name = sensor_name

    ##TODO: Missing functionality
    def is_healthy(self): raise NotImplementedError 

    ##TODO: Missing functionality
    def is_available(self): raise NotImplementedError

    def set_frequency(self, inSeconds):
        self._frequency_in_seconds = inSeconds
        pass     

    def start_monitoring(self):
        tic=0        

        try:
            while True: 
                tic += 1
                currentValue = self.read_value()

                OperatingSystem().clear_console()

                header = "Raspberry Pi - "
                header += self._name
                print("============================================================")
                print(header)
                print("============================================================")

                print("Current Value: " + str(currentValue))

                print("")
                if Config().get_enable_sim():
                    print("------------------------------------------------------------")
                    print("- WARNING! Simulator mode enabled, sensor data is NOT real -")
                    print("------------------------------------------------------------")

                footer = "*Press Cntr+C to exit monitoring "
                if tic%2 == 0: footer += "[|]"
                else: footer += "[-]"
                print(footer)

                time.sleep(self._frequency_in_seconds) 
                
        except KeyboardInterrupt:
            OperatingSystem().clear_console()            
            print("Exit Monitoring")
            time.sleep(self._frequency_in_seconds) 
            OperatingSystem().clear_console()
            pass
        pass

    @abstractmethod
    def read_value(self):  pass





