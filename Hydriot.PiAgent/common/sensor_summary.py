from datetime import datetime

class SensorSummary():
    name = None
    last_updated_increment = 0
    last_execution = None
    latest_value = None
    is_healthy = False
    _frequency_in_seconds = None
    _consecutive_error_count = 0
    _history = None
    _history_position = None
    average_reading = None
    reading_deviation = None
    is_stabilizing = True
    expect_variance = None
    lower_threshold = None
    upper_threshold = None

    _history_depth = 20
    _stabilizing_count = 5

    def _update_history_metadata(self):        
        if self._history is None or len(self._history) <= self._stabilizing_count:
            pass

        total_count = len(self._history)
        total_sum = 0
        smallest_value = self._history[0]
        largest_value = self._history[0]

        for reading in self._history:
            total_sum += reading
            
            if reading < smallest_value:
                smallest_value = reading
            if reading > largest_value:
                largest_value = reading

        self.average_reading = round((total_sum/total_count),2)
        self.reading_deviation = largest_value - smallest_value
        self.is_stabilizing = False

    def _reset_history(self):
        self._history = []
        self._history_position = 0
        self.average_reading = None
        self.reading_deviation = None
        self.is_stabilizing = True

    def _add_to_history(self, latest_value):        
        if len(self._history) < self._history_depth:
           self._history.append(latest_value)
        elif self._history_position >= len(self._history):
            self._history_position = 0
            self._history[self._history_position] = latest_value
        else:
            self._history[self._history_position] = latest_value
        self._history_position += 1

    def set_last_read_error(self):
        self._consecutive_error_count += 1
        self._reset_history()

    def __init__(self, name, frequency_in_Seconds):
        self.name = name
        self._frequency_in_seconds = frequency_in_Seconds
        self._reset_history()

    def define_health_parameters(self, expect_variance = False, lower_threshold = None, upper_threshold = None):
        self.expect_variance = expect_variance
        self.lower_threshold = lower_threshold
        self.upper_threshold = upper_threshold

    def update_value(self, new_value):
        time_now = datetime.now()
        self.last_updated_increment = -1

        if self.last_execution is not None:
            self.last_updated_increment = (time_now - self.last_execution).total_seconds()

        self.latest_value = new_value
        self.last_execution = time_now

        if new_value is not None:
            self._add_to_history(new_value)
            self._consecutive_error_count = 0
            self._update_history_metadata()
    
    def is_healthy(self):        
        has_reading = self.last_execution is None or self.latest_value is None
        has_multiple_errors = self._consecutive_error_count > 0       

        if has_reading or has_multiple_errors:
            return False

        time_passed = (datetime.now() - self.last_execution).total_seconds()
        not_updated_in_time = time_passed > (self._frequency_in_seconds * 3)

        if (not_updated_in_time):
            return False
             
        has_deviation = self.reading_deviation is not None and self.reading_deviation != 0    
        if self.expect_variance and not has_deviation:
            return False
        
        if (self.upper_threshold is not None and self.average_reading > self.upper_threshold):
            return False

        if (self.lower_threshold is not None and self.average_reading < self.lower_threshold):
            return False
        
        return True