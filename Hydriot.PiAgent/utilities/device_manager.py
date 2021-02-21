from utilities.operating_system import OperatingSystem
from utilities.config import Config
from datetime import datetime
import time
import asyncio

class DeviceManager(object):

    async def start_device_dashboard(self, sensor_list):
        toggel = False

        try:
            while True:
                toggel = not toggel

                OperatingSystem().clear_console()
                print("=====================================================")
                print("==== Available Sensors & triggers from the Agent ====")
                print("=====================================================")
                print("")

                print(">>> Registered Sensors <<<")
                for key in sensor_list:
                    sensor = sensor_list[key]
                    age_in_seconds = (datetime.now() - sensor.get_last_read_time()).total_seconds()

                    summary = f"{key} latest value is {sensor.get_latest_value()} from {round(age_in_seconds, 0)} seconds ago "
                    summary += "[ok]" if sensor.is_healthy() else "[Unhealthy]"    
                    print(summary)          

                print()

                print(">>> Registered Triggers <<<")

                if Config().get_enable_sim():
                    print("----------------------------------------------------")
                    print("WARNING! Simulator Mode Enabled")
                    pass
                
                print("----------------------------------------------------")    
                footer = "*Press Cntr+C to exit monitoring "
                footer += "[-]" if toggel else "[|]"
                print(footer)            

                await asyncio.sleep(2)
        except KeyboardInterrupt:
            self.stop_monitoring()
            OperatingSystem().clear_console()            
            print("Exit Monitoring")
            await asyncio.sleep(3) 
            OperatingSystem().clear_console()
            pass
            
        pass
