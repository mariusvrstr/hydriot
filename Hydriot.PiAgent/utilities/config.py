import os
import configparser

class Config(object):
    _configfile_name = "config.ini"

    def initialize_file(self):
        # Check if there is already a configurtion file
        if not os.path.isfile(self._configfile_name):
            # Create the configuration file as it doesn't exist yet
            cfgfile = open(self._configfile_name, "w")

            # Add content to the file
            config = configparser.ConfigParser()

            config.keys['vesion'] = 'V1.0'

            config.add_section("environment")
            config.set("environment", "os", "windows")
            
            config.write(cfgfile)
            cfgfile.close()

    def get_os(self):         
         config = configparser.ConfigParser()
         cfgfile = config.read(self._configfile_name)
         return config['environment']['os']



