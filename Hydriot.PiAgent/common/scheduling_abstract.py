from datetime import datetime
from abc import ABC, abstractmethod
import asyncio

class SchedulingAbstract(ABC):
    frequency_in_seconds = None
    _use_average = False
    _name = None
    task_manager = None

    def is_monitoring(self):
        return self.task_manager.is_task_active(self)

    def __init__(self, frequency_in_seconds, name, use_average):
        self.frequency_in_seconds = frequency_in_seconds
        self._name = name
        self._use_average = use_average

    async def run_schedule(self, task_manager):
        if (self.task_manager is None):
            self.task_manager = task_manager

        self.task_manager.add_task(self)

        while self.is_monitoring():
            if self._use_average is True:
                await self.read_average(20, 10)
            elif self._use_average is False:
                self.read_value()            
            await asyncio.sleep(self.frequency_in_seconds)            
        
        if not self.is_monitoring():
            print(f"[{self._name}] stopped.")

    def stop_schedule(self):
        print(f"Stopping [{self._name}]...")
        self.task_manager.remove_task(self)


