import asyncio
import threading

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSignal
from PyQt5.QtCore import Qt, QThread


## Single UX Worker Thread with multiple async tasksthat can be added with a group locking of dependant ones
class ThreadWrapper(QObject):
    thread = None
    tasks = dict()
    lock = None
    task_manager = None

    def __init__(self, task_manager, thread = QThread()) -> None:
        self.thread = thread
        self.lock =  threading.Lock()
        self.task_manager = task_manager

    def cleanup_task(self, task_type):
        self.lock.acquire()

        try:
            del self.tasks[task_type]
        finally:
            self.lock.release()        

    async def example_task(self, task_type):
        print(f"starting example task [{task_type}]")
        await asyncio.sleep(5)

        self.cleanup_task(task_type)
        print(f"completing example task [{task_type}]")        
    
    ##TODO: Add / Append action required
    async def run_task(self, task):
        task_type = type(task).__name__
        self.lock.acquire()

        try:
            if task_type in self.tasks:
                raise Exception("Already in progress, cannot start the same task while in progress.")

            self.tasks[task_type] = task
            self.task_manager.add_task(task_type)

        finally:
            self.lock.release()
                
        await self.example_task(task_type)
        self.task_manager.remove_task(task_type)


    