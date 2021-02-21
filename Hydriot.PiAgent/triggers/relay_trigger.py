from contracts.relay_abstract import RelayAbstract 

class RelayTrigger(RelayAbstract):
    _current_on_state = False

    def __init__(self, relay_name, default_on_state):
        RelayAbstract.__init__(self, relay_name, default_on_state)

    def _switch_relay_on(self):
        self._current_on_state = True
        pass
    
    def _switch_relay_off(self): 
        self._current_on_state = False
        pass

    def _check_if_switched_on(self): 
        return _current_on_state

    def is_available(self): 
        return True

