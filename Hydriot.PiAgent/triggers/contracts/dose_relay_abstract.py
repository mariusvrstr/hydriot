from abc import ABC, abstractmethod ## abstract module
import asyncio

class DoseRelayAbstract(ABC):
    name = "N/A"
    _is_enabled = None
    _tds_sensor = None
    _eligable = False
    _last_time_tube_was_filled = None
    
    # Cooldown period after start that will now allow dosing (In case reset mid dose)
    # Need schedule to check if eligable for dosage (Cooldown, elapsed time, sensor reading)
    # If ap switches off stop any in-progress dosing
    # Add manual dosage on schedule that also does not require TDS
    # Throw exception until calibration have taken place
    # During eligibility schedule check that dose_should_finish_by is not < now else switch relay off
    
    def __init__(self, name, is_enabled, tds_sensor_summary):
        self.name = name
        self._is_enabled = is_enabled
        self._tds_sensor = tds_sensor_summary

        if (self._is_enabled == False):
            return

        self._switch_relay_off()

    async def _dose(self, duration_in_seconds):        
        self._switch_relay_on()        
        await asyncio.sleep(duration_in_seconds)
        self._switch_relay_off()

    async def ensure_tube_is_primed(self):
        if self._last_time_tube_was_filled is None: # TODO: Add 30min cooldown for pipe fill
            await self.fill_feeder_tube()
        
    async def prime_tube_with_fluid(self):
        # microdose until average tds reading rises with more than X
        # Use the raw self._dose())
        pass

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

    def get_remaining_distance(self):
        tds_target = 180 # calculate this from TDS decline since previous dose (need history)
        tds_current_value = self._tds_sensor.current_value

        if self._tds_sensor is None:
            raise ValueError('TDS sensor not available, cannot dose on schedule')

        if tds_current_value > tds_upper_threshold or tds_current_value > tds_target_value: 
            raise ValueError('Cannot dose on schedule as TDS reading is to high already')
        
        distance = tds_target_value - tds_current_value
        return distance

    def get_duration_in_seconds_from_distance(self, tds_distance):
        tds_increase_in_a_minute = 10 # get from config that has been calibrated
        tds_upper_threshold = 500 # Get from config that can be calibrated     

        duration_in_minutes = tds_distance / tds_increase_in_a_minute

        return duration_in_minutes * 60


    async def dose_locally_from_schedule(self):      

        # Dose A - 50% of expected
        half_distance = (self.get_remaining_distance() / 2)
        duration_in_seconds = self.get_duration_in_seconds_from_distance(half_distance)
        await self.dose(duration_in_seconds)

        # Wait for dose to propagate
        await asyncio.sleep(120)

        # Execute the final dosage
        new_distance = self.get_remaining_distance()
        if half_distance < new_distance:
            new_distance = half_distance

        duration_in_seconds = self.get_duration_in_seconds_from_distance(new_distance)
        await self.dose(duration_in_seconds)        

    
    async def dose(self, duration_in_seconds):    
        self.ensure_tube_is_primed()
        # Set dose_should_finish_by timestampt
        await self._dose(duration_in_seconds)

    # Override for custom logic
    def is_enabled(self):
        return True
