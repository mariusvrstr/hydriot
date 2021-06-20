from abc import ABC, abstractmethod ## abstract module
import RPi.GPIO as GPIO
from enum import Enum

class SwitchStatus(Enum):
    Undefined = 0
    On = 1,
    Off = 2

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

    def __init__(self, name, relay_pin_pos, is_enabled, normal_status = SwitchStatus.Undefined):
        self.name = name
        self.is_enabled = is_enabled
        self._is_normally_on = normal_status == SwitchStatus.On
        self.relay_pin_pos = relay_pin_pos
        self.intended_status = normal_status

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.relay_pin_pos, GPIO.OUT)

        self.sync_status()   

    def switch_on(self):
        if not self.validate_action(SwitchStatus.On):
            print(f"Validation failed. Could not switch on [{self.name}]")
            return

        if (self._is_normally_on):
            self._switch_relay_off()
        else:
            self._switch_relay_on()

    def switch_off(self):
        if not self.validate_action(SwitchStatus.Off):
            print(f"Validation failed. Could not switch off [{self.name}]")
            return

        if (self._is_normally_on):
            self._switch_relay_on()
        else:
            self._switch_relay_off()

    def check_if_switched_on(self):
        gpio_status = GPIO.input(self.relay_pin_pos)        
        
        if self._is_normally_on:
            if gpio_status != 0:
                return True
            else:
                return False

        if not self._is_normally_on:
            if gpio_status == 0:
                return True
            else:
                return False

    ## Override if there are specific requirements to be on
    def validate_action(self, switch_status = SwitchStatus.Undefined):
        if (switch_status == SwitchStatus.Undefined):
            raise Exception("Not a valid switch action")

        return True

    ## override if you want more specific rules
    def sync_status(self):
        self.switch_off()