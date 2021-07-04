import RPi.GPIO as GPIO

from triggers.contracts.dose_relay_abstract import DoseRelayAbstract
from settings.app_config import AppConfig
from settings.trigger_config import TriggerConfig

class NutrientDispenserRelayStub(DoseRelayAbstract):
    _actual_on_state = False    

    def __init__(self):
        enabled = AppConfig().is_nutrient_dispenser_enabled()
        DoseRelayAbstract.__init__(self, "Nutrient Dispenser Switch", enabled, TriggerConfig().get_tds_max_prime_time())

    def _switch_relay_on(self):
        self._actual_on_state = True
        pass
    
    def _switch_relay_off(self): 
        self._actual_on_state = False
        pass

    def check_if_switched_on(self):
        return self._actual_on_state

class NutrientDispenserRelay(DoseRelayAbstract):
    relay_pin_pos = 32 # Which PIN is used on the Pi
    is_low_volt_relay = True # Use this when connected to 3.3V source (If it does switch off use this and switch to 3.3V)

    def __init__(self):
        enabled = AppConfig().is_nutrient_dispenser_enabled()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.relay_pin_pos, GPIO.OUT) # GPIO Assign mode
        DoseRelayAbstract.__init__(self, "Nutrient Dispenser Switch", enabled, TriggerConfig().get_tds_max_prime_time())

    def set_dependant_sensor_summary(self, tds_sensor_summary):
        self._counter_sensor = tds_sensor_summary