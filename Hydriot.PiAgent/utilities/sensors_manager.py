from utilities.config import Config
from utilities.dependency_injection import Container
from utilities.operating_system import OperatingSystem
from utilities.config import Config
from datetime import datetime
import time
import asyncio

class SensorsManager(object):
    sensor_list = dict()

    def register_one(self, sensor_name, sensor):
        self.sensor_list[sensor_name] = sensor
        pass

    def register_available(self):       
        container = Container()

        # How to register multiple?
        tds_sensor = container.tds_factory() 

        if tds_sensor.is_available():
            self.register_one("TDS", tds_sensor)
            pass

        water_level_sensor = container.water_level_sensor_factory()
        if water_level_sensor.is_available():
            self.register_one("WaterLevel", water_level_sensor)
            pass

    def start_monitoring(self):
        for key in self.sensor_list:
            sensor = self.sensor_list[key]
            asyncio.ensure_future(sensor.start_monitoring())  
     
        pass

    def stop_monitoring(self):
        for key in self.sensor_list:
            sensor = self.sensor_list[key]
            sensor.stop_monitoring()
        pass


    async def monitor_sensors(self):
        toggel = False

        try:
            while True:
                toggel = not toggel

                OperatingSystem().clear_console()
                print("====================================================")
                print("==== Available Sensor Readings from the Pi Agen ====")
                print("====================================================")
                print("")

                for key in self.sensor_list:
                    sensor = self.sensor_list[key]
                    age_in_seconds = (datetime.now() - sensor.get_last_read_time()).total_seconds()

                    summary = f"{key} latest value is {sensor.get_latest_value()} from {round(age_in_seconds, 0)} seconds ago "
                    summary += "[ok]" if sensor.is_healthy() else "[Unhealthy]"    
                    print(summary)          

                print()

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
