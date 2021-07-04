from triggers.contracts.on_off_relay_abstract import OnOffRelayAbstract, SwitchStatus
from settings.app_config import AppConfig

# TODO: Configurable pump cutout if water level drop below minimum water

class WaterPumpRelayStub(OnOffRelayAbstract):
    _actual_on_state = False

    def __init__(self):
        enabled = AppConfig().is_water_pump_enabled()
        OnOffRelayAbstract.__init__(self, "Water Pump", enabled, SwitchStatus.On)

    def _switch_relay_on(self):
        self._actual_on_state = True
        pass
    
    def _switch_relay_off(self): 
        self._actual_on_state = False
        pass

    def _check_if_switched_on(self): 
        return self._actual_on_state


class WaterPumpRelay(OnOffRelayAbstract):
    relay_pin_pos = 38 # Which PIN is used on the Pi    
    water_sensor = None

    def __init__(self):        
        enabled = AppConfig().is_water_pump_enabled()       
        OnOffRelayAbstract.__init__(self, "Water Pump", self.relay_pin_pos, enabled, SwitchStatus.On)

    def set_dependant_sensor_summary(self, water_sensor):
        self.water_sensor = water_sensor

    ## TODO: This should be converted to a observer pattern
    def sync_status(self):        

        if self.water_sensor is None or self.water_sensor.latest_value is None:
            return

        currently_on = self.check_if_switched_on()
        detect_water = self.water_sensor.latest_value == 1

        if currently_on and not detect_water:
            self.switch_off()

        elif self._is_normally_on and detect_water:
            self.switch_on()       

    def validate_action(self, action):
        if (action == SwitchStatus.Undefined):
            raise Exception("Not a valid switch action")

        if action == SwitchStatus.On and self.water_sensor.latest_value != 1:
            return False

        return True