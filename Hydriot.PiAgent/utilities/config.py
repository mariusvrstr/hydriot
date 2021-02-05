import os
import configparser
from utilities.operating_system import OperatingSystem

class Config(object):
    _configfile_name = "config.ini"

    def initialize_file(self):
        # Check if there is already a configurtion file
        if not os.path.isfile(self._configfile_name):
            # Create the configuration file as it doesn't exist yet
            cfgfile = open(self._configfile_name, "w")

            # Add content to the file
            config = configparser.ConfigParser()

            config.add_section("environment")
            config.set("environment", "os", OperatingSystem().name())
            config.set("environment", "enable_sim", "true")
           
            config.write(cfgfile)
            cfgfile.close()

    def get_os(self):         
         config = configparser.ConfigParser()
         cfgfile = config.read(self._configfile_name)
         return config['environment']['os']

    def get_enable_sim(self):           
        config = configparser.ConfigParser()
        cfgfile = config.read(self._configfile_name)
        simulater_enabled = config['environment']['enable_sim'] == "true"
        return simulater_enabled


