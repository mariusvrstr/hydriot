import platform
import os

class OperatingSystem(object):   
    def name(self):
        return platform.system()

    def clear_console(self):
        if self.name() == 'Windows':
            os.system('cls')
        elif self.name() == 'Linux':
            os.system('clear')
        else:
            print('Unknown Operating System')
        pass