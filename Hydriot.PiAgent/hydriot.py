from contracts.sensor_summary import SensorSummary

class Hydriot():
    tds_sensor = None
    water_level_sensor = None
    ph_sensor = None

    water_pump_relay = None
    light_relay = None

    def set_tds_sensor(self, tds_sensor):
        self.tds_sensor = tds_sensor

    def set_water_level_sensor(self, water_level_sensor):
        self.water_level_sensor = water_level_sensor



    
    

