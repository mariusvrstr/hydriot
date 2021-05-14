
class Hydriot():
    tds_sensor = None
    water_level_sensor = None
    ph_sensor = None
    light_sensor_infrared = None

    water_pump_trigger = None
    light_trigger = None
    
    add_nutrient_trigger = None
    lower_ph_trigger = None

    def set_tds_sensor(self, tds_sensor):
        self.tds_sensor = tds_sensor

    def set_water_level_sensor(self, water_level_sensor):
        self.water_level_sensor = water_level_sensor
    
    def set_ph_sensor(self, ph_sensor):
        self.ph_sensor = ph_sensor

    def set_light_sensor_infrared(self, light_sensor_infrared):
        self.light_sensor_infrared = light_sensor_infrared

    

    def set_water_pump_trigger(self, water_pump_trigger):
        self.water_pump_trigger = water_pump_trigger

    def set_light_trigger(self, light_trigger):
        self.light_trigger = light_trigger

    
    

    
    

