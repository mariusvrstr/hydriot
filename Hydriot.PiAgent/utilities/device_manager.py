from utilities.operating_system import OperatingSystem
from utilities.config import Config
from datetime import datetime
import RPi.GPIO as GPIO
import time
import asyncio

class DeviceManager(object):

    def get_sensor_summary(self, sensor_summary):
        age_in_seconds = "N/A" if sensor_summary.last_execution is None else round((datetime.now() - sensor_summary.last_execution).total_seconds(), 0)
        latest_value = "N/A" if sensor_summary.latest_value is None else sensor_summary.latest_value

        summary = f"{sensor_summary.name} latest value is [{latest_value}] from [{age_in_seconds}] seconds ago "
        summary += "[ok]" if sensor_summary.is_healthy() else "[Unhealthy]"    

        return summary

    async def start_device_dashboard(self, hydriot, trigger_manager, integration_adapter):
        toggel = False

        try:
            while True:
                toggel = not toggel

                OperatingSystem().clear_console()
                print("Hydriot Node")
                print("=====================================================")
                print()

                print(">>> Registered Sensors <<<")

                if hydriot.tds_sensor is not None:
                    print(self.get_sensor_summary(hydriot.tds_sensor))
                if hydriot.water_level_sensor is not None:
                    print(self.get_sensor_summary(hydriot.water_level_sensor))

                print()
                print(">>> Registered Triggers <<<")
                for key in trigger_manager.trigger_list:
                    trigger = trigger_manager.trigger_list[key]
                    current_on_status = trigger.is_switched_on()

                    status = "On" if current_on_status else "Off"

                    summary = f"{key} is switched [{status}]" # get last changed time
                    ##summary += "[ok]" if sensor.is_healthy() else "[Unhealthy]"    
                    print(summary)       

                print()
                print(">>> Integration Status <<<")
                status = "Connected" if integration_adapter.previous_integration_success else "Disconnected"
                last_update = "N/A" if integration_adapter.last_integration_update == None else integration_adapter.last_integration_update
                print(f"Connection status: [{status}] last updated [{last_update}]")

                print()
                if Config().get_enable_sim():
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
