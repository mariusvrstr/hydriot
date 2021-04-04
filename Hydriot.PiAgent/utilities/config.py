import os
import configparser
from utilities.operating_system import OperatingSystem

class Config(object):
    _configfile_name = "config.ini"

    # sections
    environment_section = "environment"
    integration_api_section = "integration_api"
    
    def __init__(self):
        # Check if there is already a configurtion file
        if not os.path.isfile(self._configfile_name):
            # Create the configuration file as it doesn't exist yet
            cfgfile = open(self._configfile_name, "w")

            # Add content to the file
            config = configparser.ConfigParser()

            config.add_section(self.environment_section)
            config.set(self.environment_section, "os", OperatingSystem().name())
            config.set(self.environment_section, "enable_sim", "true")

            config.add_section(self.integration_api_section)
            config.set(self.integration_api_section, "base_url", "https://localhost:44333/api")
            config.set(self.integration_api_section, "node_id", "508728DE-F6AC-48C9-9D12-F18E0674A70A") # TODO: replace with n/a
            config.set(self.integration_api_section, "user", "****")
            config.set(self.integration_api_section, "pass", "****")
           
            config.write(cfgfile)
            cfgfile.close()
    
    def get_key_value(self, section, key):
        config = configparser.ConfigParser() 
        cfgfile = config.read(self._configfile_name)
        return config[section][key]

    def get_os(self):       
        return self.get_key_value(self.environment_section, "os")

    def get_enable_sim(self):
        return self.get_key_value(self.environment_section, "enable_sim") == "true"

    def get_integration_node_id(self):
        return self.get_key_value(self.integration_api_section, "node_id")

    def get_integration_api_base_url(self):
        return self.get_key_value(self.integration_api_section, "base_url")

    def get_integration_api_username(self):
        return self.get_key_value(self.integration_api_section, "user")

    def get_integration_api_password(self):
        return self.get_key_value(self.integration_api_section, "pass")