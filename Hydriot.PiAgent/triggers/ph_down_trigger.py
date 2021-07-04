from triggers.contracts.dose_relay_abstract import DoseRelayAbstract
import RPi.GPIO as GPIO
from settings.app_config import AppConfig
from settings.trigger_config import TriggerConfig

class PhDownRelayStub(DoseRelayAbstract):
    _actual_on_state = False   

    def __init__(self):
        enabled = AppConfig().is_ph_down_enabled()
        DoseRelayAbstract.__init__(self, "Ph-Down Switch", enabled, TriggerConfig().get_ph_down_max_prime_time())

    def _switch_relay_on(self):
        self._actual_on_state = True
        pass
    
    def _switch_relay_off(self): 
        self._actual_on_state = False
        pass

    def check_if_switched_on(self):
        return self._actual_on_state


class PhDownRelay(DoseRelayAbstract):    
    relay_pin_pos = 36 # Which PIN is used on the Pi
    is_low_volt_relay = True # Use this when connected to 3.3V source (If it does switch off use this and switch to 3.3V)

    def __init__(self):     
        enabled = AppConfig().is_ph_down_enabled()   
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.relay_pin_pos, GPIO.OUT) # GPIO Assign mode
        DoseRelayAbstract.__init__(self, "Ph-Down Switch", enabled, TriggerConfig().get_ph_down_max_prime_time())

    def set_dependant_sensor_summary(self, ph_down_sensor_summary):
        self._counter_sensor = ph_down_sensor_summary
