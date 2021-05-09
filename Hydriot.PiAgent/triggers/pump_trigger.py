from triggers.contracts.on_off_relay_abstract import OnOffRelayAbstract
import RPi.GPIO as GPIO
import time

# TODO: Configurable pump cutout if water level drop below minimum water

class PumpRelayStub(OnOffRelayAbstract):
    _actual_on_state = False

    def __init__(self):
        OnOffRelayAbstract.__init__(self, "Pump Switch", False, True)

    def _switch_relay_on(self):
        self._actual_on_state = True
        pass
    
    def _switch_relay_off(self): 
        self._actual_on_state = False
        pass

    def _check_if_switched_on(self): 
        return self._actual_on_state

    def is_available(self): 
        return True

class PumpRelay(OnOffRelayAbstract):
    relay_pin_pos = 36 # Which PIN is used on the Pi
    is_low_volt_relay = True # Use this when connected to 3.3V source (If it does switch off use this and switch to 3.3V)

    def __init__(self):        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.relay_pin_pos, GPIO.OUT) # GPIO Assign mode
        OnOffRelayAbstract.__init__(self, "Pump Switch", True, True) # Start either ON or OFF

    def _switch_relay_on(self):
        self._current_on_state = True
        GPIO.output(self.relay_pin_pos, GPIO.LOW if self.is_low_volt_relay else GPIO.HIGH) # ON
        pass
    
    def _switch_relay_off(self): 
        GPIO.output(self.relay_pin_pos, GPIO.HIGH if self.is_low_volt_relay else GPIO.LOW) # OFF
        pass

    def _check_if_switched_on(self): 
        gpio_status = GPIO.input(self.relay_pin_pos)
        return gpio_status == 0 # On

    def is_available(self): 
        return True

