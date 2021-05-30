
from configparser import NoSectionError

class Hydriot():
    tds_sensor = None
    water_level_sensor = None
    ph_sensor = None
    light_sensor_infrared = None
    voltage_tester = None

    water_pump_trigger = None 
    nutrient_disposer_trigger = None
    ph_down_trigger = None

    def set_tds_sensor(self, tds_sensor):
        self.tds_sensor = tds_sensor

    def set_water_level_sensor(self, water_level_sensor):
        self.water_level_sensor = water_level_sensor
    
    def set_ph_sensor(self, ph_sensor):
        self.ph_sensor = ph_sensor

    def set_light_sensor_infrared(self, light_sensor_infrared):
        self.light_sensor_infrared = light_sensor_infrared

    def set_voltage_tester(self, voltage_tester):
        self.voltage_tester = voltage_tester

    def set_nutrient_disposer_trigger(self, nutrient_disposer_trigger):
        self.nutrient_disposer_trigger = nutrient_disposer_trigger
    
    def set_ph_down_trigger(self, ph_down_trigger):
        self.ph_down_trigger = ph_down_trigger

    def set_water_pump_trigger(self, water_pump_trigger):
        self.water_pump_trigger = water_pump_trigger



    
    

    
    

