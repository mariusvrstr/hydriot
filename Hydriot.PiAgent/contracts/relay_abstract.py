
class RelayAbstract(ABC):
    _name = "N/A"
    _current_on_state = False
    _is_monitoring = False
    _sync_frequency_in_seconds = 5 #TODO: Make 60 after testing

    def __init__(self, relay_name, default_on_state):
        self._name = relay_name    
        
        if (default_on_state):
            self.switch_on()
    
    def is_switched_on(self):
        return self._current_on_state  

    def stop_sync(self):
        self._is_monitoring = False   

    async def start_sync(self):
        self._is_monitoring = True

        while self._is_monitoring:            
            self.sync_status()
            await asyncio.sleep(self._sync_frequency_in_seconds)
        pass    

    ## Ensure expected state is = to current state
    def sync_status(self): 
        actual_on_state = _check_if_switched_on()

        if _current_on_state == actual_on_state:
            pass
        elif _current_on_state and (actual_on_state == False):
            print('Warning! Relay is out of sync - Switching ON')
            self.switch_on()
        elif (_current_on_state == False) and actual_on_state:
            print('Warning! Relay is out of sync - Switching OFF')
            self.switch_off()
        else:
            pass
    
    def switch_on(self):        
        if _is_monitoring == False:
            self.start_sync()

        self._switch_relay_on()
        pass

    def switch_off(self): 
        self._switch_relay_off()

        if _is_monitoring:
            self.stop_sync()       
        pass

    @abstractmethod
    def _switch_relay_on(self): raise NotImplementedError

    @abstractmethod
    def _switch_relay_off(self): raise NotImplementedError

    @abstractmethod
    def _check_if_switched_on(self): raise NotImplementedError

    @abstractmethod
    def is_available(self): raise NotImplementedError