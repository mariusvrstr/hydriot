from datetime import datetime
from abc import ABC, abstractmethod

import asyncio

class SchedulingAbstract(ABC):

    frequency_in_seconds = None
    _is_monitoring = False

    def __init__(self, frequency_in_seconds):
        self.frequency_in_seconds = frequency_in_seconds   

    async def run_schedule(self):
        self._is_monitoring = True

        while self._is_monitoring:
            self.read_value()
            await asyncio.sleep(self.frequency_in_seconds)            
        pass

    def stop_schedule(self):
        self._is_monitoring = False

