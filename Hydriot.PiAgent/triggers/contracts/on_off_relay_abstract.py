from abc import ABC, abstractmethod ## abstract module
import RPi.GPIO as GPIO

class OnOffRelayAbstract(ABC):
    name = "N/A"
    is_enabled = None
    _is_normally_on = None
    relay_pin_pos = None
    is_low_volt_relay = True # Use this when connected to 3.3V source (If it does switch off use this and switch to 3.3V)

    def _switch_relay_on(self):
        self._current_on_state = True
        GPIO.output(self.relay_pin_pos, GPIO.LOW if self.is_low_volt_relay else GPIO.HIGH) # ON
        pass
    
    def _switch_relay_off(self): 
        GPIO.output(self.relay_pin_pos, GPIO.HIGH if self.is_low_volt_relay else GPIO.LOW) # OFF
        pass

    def _sync_to_defaults(self):
        if (self.is_normally_on):
            self.switch_on()
        else:
            self.switch_off()

    def __init__(self, name, relay_pin_pos, is_enabled, is_normally_on = False):
        self.name = name
        self.is_enabled = is_enabled
        self._is_normally_on = is_normally_on
        self.relay_pin_pos = relay_pin_pos

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.relay_pin_pos, GPIO.OUT)

        if (not self.is_enabled):
            return

        self._sync_to_defaults()        

    def switch_on(self):
        if (self._is_normally_on):
            self._switch_relay_off()
        else:
            self._switch_relay_on()

    def switch_off(self):
        if (self._is_normally_on):
            self._switch_relay_on()
        else:
            self._switch_relay_off()

    def check_if_switched_on(self):
        self.sync_status()

        gpio_status = GPIO.input(self.relay_pin_pos)        
        
        if self._is_normally_on and gpio_status != 0:
            return True

        if not self._is_normally_on and gpio_status == 0:
            return True

        return False

    ## Override if there are specific requirements to be on
    def sync_status(self):
        pass