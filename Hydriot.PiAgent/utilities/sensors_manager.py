from utilities.config import Config
from utilities.dependency_injection import Container
from utilities.operating_system import OperatingSystem
from utilities.config import Config
from datetime import datetime
from sensors.tds_sensor import TDSSensorStub, TDSSensor
from sensors.water_level_sensor import WaterLevelSensorStub, WaterLevelSensor
import time
import asyncio

class SensorsManager(object):
    sensor_list = dict()

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

    def register_one(self, sensor_name, sensor):
        self.sensor_list[sensor_name] = sensor
        pass

    def register_available(self):       
        container = Container()

        # How to register multiple?
        tds_sensor =  container.tds_factory() 

        if tds_sensor.is_available():
            self.register_one("TDS", tds_sensor)
            pass

        water_level_sensor = container.water_level_sensor_factory()

        if water_level_sensor.is_available():
            self.register_one("WaterLevel", water_level_sensor)
            pass

   


