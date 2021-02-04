from utilities.config import Config
from utilities.operating_system import OperatingSystem

class Device(object):
    def Boot(self):
        Config().initialize_file()
    pass
