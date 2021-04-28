from datetime import datetime
from abc import ABC, abstractmethod

import asyncio

class SchedulingAbstract(ABC):

    frequency_in_seconds = None
    _is_monitoring = False
    _name = None

    def __init__(self, frequency_in_seconds, name):
        self.frequency_in_seconds = frequency_in_seconds
        self._name = name

    async def run_schedule(self):
        self._is_monitoring = True

        while self._is_monitoring:
            self.read_value()
            await asyncio.sleep(self.frequency_in_seconds)            
        
        if self._is_monitoring:
            print(f"[{self._name}] stopped.")

    def stop_schedule(self):
        print(f"Stopping [{self._name}]...")
        self._is_monitoring = False


