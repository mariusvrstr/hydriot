from abc import ABC, abstractmethod ## abstract module
from datetime import datetime, timedelta

import RPi.GPIO as GPIO
import asyncio

class DoseRelayAbstract(ABC):
    name = "N/A"
    is_enabled = None
    _counter_sensor = None
    _eligable = False
    _last_time_tube_was_filled = None
    _maximum_prime_time = None
    _is_dosing = False
    
    # Cooldown period after start that will now allow dosing (In case reset mid dose)
    # Need schedule to check if eligable for dosage (Cooldown, elapsed time, sensor reading)
    # If ap switches off stop any in-progress dosing
    # Add manual dosage on schedule that also does not require TDS
    # Throw exception until calibration have taken place
    # During eligibility schedule check that dose_should_finish_by is not < now else switch relay off

    async def _dose(self, duration_in_seconds):     
        self._is_dosing = True   
        self._switch_relay_on()        
        await asyncio.sleep(duration_in_seconds)
        self._switch_relay_off()
        self._is_dosing = False

    def _switch_relay_on(self):
        self._current_on_state = True
        GPIO.output(self.relay_pin_pos, GPIO.LOW if self.is_low_volt_relay else GPIO.HIGH) # ON
        pass
    
    def _switch_relay_off(self): 
        GPIO.output(self.relay_pin_pos, GPIO.HIGH if self.is_low_volt_relay else GPIO.LOW) # OFF
        pass

    def __init__(self, name, is_enabled, max_prime_time):
        self.name = name
        self.is_enabled = is_enabled
        self._maximum_prime_time = max_prime_time
        self._switch_relay_off()

    def check_if_switched_on(self): 
        gpio_status = GPIO.input(self.relay_pin_pos)
        return gpio_status == 0 # relay is switched on

    async def prime_tube_with_fluid(self):
        avg_deviation = None
        start_measurement = None
        self._is_dosing = True

        if self._counter_sensor is not None:
            avg_deviation = self._counter_sensor.reading_deviation
            start_measurement = self._counter_sensor.latest_value

        self._switch_relay_on()
        prime_time_end = datetime.now() + timedelta(seconds=self._maximum_prime_time)

        while (datetime.now() <= prime_time_end):
            await asyncio.sleep(1)
            
            if self._counter_sensor is not None:
                startingToInfluenceTds =  self._counter_sensor.latest_value > (start_measurement + avg_deviation)
                if startingToInfluenceTds:
                    break

        self._switch_relay_off()
        self._is_dosing = False

    def dose_with_online_pid_controller(self):        
        if not self._eligable:
            raise ValueError('Trying to dose while not in being in a correct state')         

        # 1. Negotiate a new dose session with online service (return with frequency)
        # 2. While not complete loop to server
            # a. Read TDS and check if completed (within x TDS from target)
            # b. Request dosage instructions (return dose_duration_in_seconds and sleep time)
            # c. Dose
            # d. Sleep
        pass

    async def dose(self, duration_in_seconds):
        await self.prime_tube_with_fluid()
        await self._dose(duration_in_seconds)

    def busy_dosing(self):
        # Move this out of memory to accommodate use across threads
        return self._is_dosing
