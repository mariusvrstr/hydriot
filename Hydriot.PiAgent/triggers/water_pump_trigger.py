from triggers.contracts.on_off_relay_abstract import OnOffRelayAbstract
import RPi.GPIO as GPIO
from settings.app_config import AppConfig

# TODO: Configurable pump cutout if water level drop below minimum water

class WaterPumpRelayStub(OnOffRelayAbstract):
    _actual_on_state = False

    def __init__(self):
        enabled = AppConfig().is_water_pump_enabled()
        OnOffRelayAbstract.__init__(self, "Water Pump Switch", enabled, True)

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
    is_low_volt_relay = True # Use this when connected to 3.3V source (If it does switch off use this and switch to 3.3V)
    water_sensor = None

    def __init__(self):        
        enabled = AppConfig().is_water_pump_enabled()
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.relay_pin_pos, GPIO.OUT) # GPIO Assign mode
        OnOffRelayAbstract.__init__(self, "Water Pump Switch", enabled, True) # Start either ON or OFF

    def set_water_level_sensor(self, water_sensor):
        self.water_sensor = water_sensor

    def sync_status(self):
        if self.water_sensor is None:
            return
        
        if self.water_sensor.latest_value != 1:
            print("Switching water pump off, water not detected.")
            self.switch_off()
        else:
            self.switch_on()