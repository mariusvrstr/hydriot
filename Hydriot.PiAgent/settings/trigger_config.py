import os
import configparser

class TriggerConfig(object):
    _configfile_name = "config_triggers.ini"

    # sections
    nutrient_section = "nutrient_dispenser"
    ph_section = "ph_down_dispenser"
    
    def __init__(self):
        # Check if there is already a configuration file
        if not os.path.isfile(self._configfile_name):
            # Create the configuration file as it doesn't exist yet
            cfgfile = open(self._configfile_name, "w")

            # Add content to the file
            config = configparser.ConfigParser()

            config.add_section(self.nutrient_section)
            config.set(self.nutrient_section, "max_prime_time_seconds", "5")
            config.set(self.nutrient_section, "tds_per_20_seconds", "8")
            config.set(self.nutrient_section, "dose_time_seconds", "20")
           
            config.write(cfgfile)
            cfgfile.close()
    
    def get_key_value(self, section, key):
        config = configparser.ConfigParser() 
        cfgfile = config.read(self._configfile_name)
        return config[section][key]

    def get_max_prime_time(self):       
        return int(self.get_key_value(self.nutrient_section, "max_prime_time_seconds"))

    def get_tds_per_20_seconds(self):       
        return int(self.get_key_value(self.nutrient_section, "tds_per_20_seconds"))

    def get_dose_time_seconds(self):       
        return int(self.get_key_value(self.nutrient_section, "dose_time_seconds"))