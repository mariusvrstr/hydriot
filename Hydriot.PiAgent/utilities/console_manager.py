from utilities.app_config import AppConfig
from datetime import datetime
import RPi.GPIO as GPIO
import time
import asyncio
import platform
import os

class ConsoleManager(object):

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

    async def start_device_dashboard(self, hydriot, integration_adapter):
        toggel = False

        try:
            while True:
                toggel = not toggel

                ConsoleManager().clear_console()
                print("Hydriot Node")
                print("=====================================================")
                print()

                print(">>> Registered Sensors <<<")

                if hydriot.tds_sensor is not None:
                    print(self.get_sensor_summary(hydriot.tds_sensor))
                if hydriot.water_level_sensor is not None:
                    print(self.get_sensor_summary(hydriot.water_level_sensor))
                if hydriot.ph_sensor is not None:
                    print(self.get_sensor_summary(hydriot.ph_sensor))
                if hydriot.voltage_tester is not None:
                    print(self.get_sensor_summary(hydriot.voltage_tester))

                print()
                print(">>> Registered Triggers <<<")

                if hydriot.light_trigger is not None:
                    print(self.get_trigger_summary(hydriot.light_trigger))
                if hydriot.water_pump_trigger is not None:
                    print(self.get_trigger_summary(hydriot.water_pump_trigger)) 

                print()
                print(">>> Integration Status <<<")
                status = "Connected" if integration_adapter.previous_integration_success else "Disconnected"
                last_update = "N/A" if integration_adapter.last_integration_update == None else integration_adapter.last_integration_update
                print(f"Connection status: [{status}] last updated [{last_update}]")

                print()
                if AppConfig().get_enable_sim():
                    print("WARNING! Simulator Mode Enabled")
                    pass
                                
                print("----------------------------------------------------")    
                footer = "*Press Cntr+C to exit monitoring "
                footer += "[-]" if toggel else "[|]"
                print(footer)
                print()

                await asyncio.sleep(2)

        except KeyboardInterrupt:
            pass            
        pass
