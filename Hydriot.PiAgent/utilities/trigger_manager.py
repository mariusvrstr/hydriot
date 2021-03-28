from utilities.dependency_injection import Container
import RPi.GPIO as GPIO
from utilities.config import Config

class TriggerManager(object):
    trigger_list = dict()
    container = Container()
    
    def register_one(self, trigger_name, trigger):
        self.trigger_list[trigger_name] = trigger
        pass

    def register_available(self):
        light_relay = self.container.light_relay_factory()
        pump_relay = self.container.pump_relay_factory()

        if light_relay.is_available():
            self.register_one("Light Relay", light_relay)
            self.register_one("Pump Relay", pump_relay)
            pass
        pass

    def cleanup(self):
        for key in self.trigger_list:
            trigger = self.trigger_list[key]
            trigger.stop_sync()      

        if Config().get_enable_sim() == False:
            GPIO.cleanup()
            
        pass