from abc import ABC, abstractmethod ## abstract module

class OnOffRelayAbstract(ABC):
    name = "N/A"
    _expected_on_state = False
    _is_enabled = None

    def _determine_expected_on_state(self, default_on_state):
        # TODO: Go to cloud and determine what the state should be

        if (self.is_enabled() and default_on_state):
            self._expected_on_state = True

    def check_if_switched_on(self):
        self._expected_on_state = self._check_if_switched_on()
        return self._expected_on_state

    def __init__(self, name, default_on_state, is_enabled):
        self.name = name
        self._is_enabled = is_enabled

        if (self._is_enabled == False):
            return

        self._determine_expected_on_state(default_on_state)
        self.sync_status()  

    def sync_status(self):
        actual_on_state = self._check_if_switched_on()  

        if self._expected_on_state and (actual_on_state == False):
            # Expected is ON and Actual is OFF = Switch on
            self._switch_relay_on() 
        
        elif (self._expected_on_state == False) and actual_on_state:
            # Expected is OFF and Actual is ON = Switch OFF
            self._switch_relay_off()
    
    def switch_on(self):        
        self._switch_relay_on()
        self._expected_on_state = True
        pass

    def switch_off(self): 
        self._switch_relay_off()
        self._expected_on_state = False

    @abstractmethod
    def _switch_relay_on(self): raise NotImplementedError

    @abstractmethod
    def _switch_relay_off(self): raise NotImplementedError

    @abstractmethod
    def _check_if_switched_on(self): raise NotImplementedError

    # Override for custom logic
    def is_enabled(self):
        return True