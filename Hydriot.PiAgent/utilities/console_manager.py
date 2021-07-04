import platform
import os

from configparser import Error
from settings.app_config import AppConfig
from datetime import datetime

class ConsoleManager(object):
    toggle = True
    _save_to_file = False
    _last_save_timestamp = None

    def writeline(self, line = "", file = None):
        print(line)

        if (file is not None):
            file.write(f"Timestamp [{datetime.now()}] >> {line}\n")

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

    def get_sensor_summary(self, sensor_summary):

        age_in_seconds = None if sensor_summary.last_execution is None else round((datetime.now() - sensor_summary.last_execution).total_seconds(), 0)
        latest_value = None if sensor_summary.latest_value is None else sensor_summary.latest_value
        default_display = "n/a"

        summary = f"{sensor_summary.name} latest reading is "
        summary += "[" + ("~" if sensor_summary.is_stabilizing else "")
        summary += (default_display if latest_value is None else str(latest_value)) + "] "
        summary += "from [" + (default_display if age_in_seconds is None else str(age_in_seconds)) + "] seconds ago. "
        summary += "AVG [" + (default_display if sensor_summary.average_reading is None else str(round(sensor_summary.average_reading,2))) + "] "
        summary += "DEV [" + (default_display if sensor_summary.reading_deviation is None else str(round(sensor_summary.reading_deviation,2))) + "] "
        summary += ">>> " + ("HEALTHY" if sensor_summary.is_healthy() else "UNHEALTHY") + " <<<"

        return summary

    def get_trigger_summary(self, trigger):
        current_on_status = trigger.check_if_switched_on()
        status = "On" if current_on_status else "Off"
        summary = f"{trigger.name} is switched [{status}]"
        
        return summary

    def prepare_file(self, filePath):

        if (".txt" not in filePath):
            raise Error("Incorrect file specified")

        ## Only save to file every minute
        if (self._last_save_timestamp is not None and (datetime.now() - self._last_save_timestamp).total_seconds() < 60):
            return None

        file = open(filePath,"a", encoding="utf-8")
        self._last_save_timestamp = datetime.now()
        return file

    def display_sensors(self, hydriot, integration_adapter, task_manager):
        ConsoleManager().clear_console()
        config = AppConfig()
        self._save_to_file = config.get_save_to_file()
        file = None

        if (self._save_to_file):
            file = self.prepare_file("output.txt")

        print("Hydriot Node")
        print("=====================================================")
        print("")

        print(">>> Registered Sensors <<<")

        if hydriot.tds_sensor is not None:
            print(self.get_sensor_summary(hydriot.tds_sensor))
        if hydriot.water_level_sensor is not None:
            print(self.get_sensor_summary(hydriot.water_level_sensor))
        if hydriot.ph_sensor is not None:
            print(self.get_sensor_summary(hydriot.ph_sensor))
        if hydriot.voltage_sensor is not None:
            self.writeline(self.get_sensor_summary(hydriot.voltage_sensor), file)

        print("")
        print(">>> Registered Triggers <<<")

        if hydriot.water_pump_trigger is not None and hydriot.water_pump_trigger.is_enabled:
                print(self.get_trigger_summary(hydriot.water_pump_trigger))

        if hydriot.nutrient_trigger is not None and hydriot.nutrient_trigger.is_enabled:
                print(self.get_trigger_summary(hydriot.nutrient_trigger))
        
        if hydriot.ph_trigger is not None and hydriot.ph_trigger.is_enabled:
                print(self.get_trigger_summary(hydriot.ph_trigger))

        print()
        print(">>> Integration Status <<<")
        status = "Connected" if integration_adapter.previous_integration_success else "Disconnected"
        last_update = "N/A" if integration_adapter.last_integration_update == None else integration_adapter.last_integration_update
        print(f"Connection status: [{status}] last updated [{last_update}]")

        print()
        if config.get_enable_sim():
            print("WARNING! Simulator Mode Enabled")
            pass

        task_list = ""
        for key in task_manager.tasks:
            task_list += f"[{key}] "

        print(f"Active tasks: {task_list}")
                        
        print("----------------------------------------------------")    
        footer = "*Press Cntr+C to exit monitoring "
        footer += "[-]" if self.toggle else "[|]"
        print(footer)
        print("")

        if (file is not None):
            file.close()

        self.toggle = not self.toggle

