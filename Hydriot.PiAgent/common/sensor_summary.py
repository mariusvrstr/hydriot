from datetime import datetime

class SensorSummary():
    name = None
    last_updated_increment = 0
    last_execution = None
    latest_value = None
    is_healthy = False
    _frequency_in_seconds = None

    def __init__(self, name, frequency_in_Seconds):
        self.name = name
        self._frequency_in_seconds = frequency_in_Seconds
        pass

    def update_value(self, new_value):
        time_now = datetime.now()
        self.last_updated_increment = -1

        if self.last_execution is not None:
            self.last_updated_increment = (time_now - self.last_execution).total_seconds()

        self.latest_value = new_value
        self.last_execution = time_now
    
    def is_healthy(self):
        if self.last_execution is None or self.latest_value is None:
            return False
             
        time_passed = (datetime.now() - self.last_execution).total_seconds()

        if time_passed > (self._frequency_in_seconds * 3):
            return False
        
        return True