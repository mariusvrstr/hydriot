from utilities.config import Config
from utilities.dependency_injection import Container

class Sensors(object):
    def RegisterAvailable(self):       
        container = Container()

        tds_sensor = container.tds_factory()
        if tds_sensor.is_healthy():
            tds_sensor.start_monitoring()
            pass

        water_level_sensor = container.water_level_sensor_factory()
        if water_level_sensor.is_healthy():
            water_level_sensor.start_monitoring()
            pass
