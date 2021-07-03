import threading

class TaskManager():
    tasks = dict()
    lock = None

    def __init__(self) -> None:
        self.lock =  threading.Lock()

    def add_task(self, key, task):
        self.lock.acquire()

        try:
            if key in self.tasks:
                raise Exception(f"Cannot add task [{key}] one is already existing.")
            self.tasks[key] = task
        finally:
            self.lock.release()

    def add_update_task(self, key, task):
        self.lock.acquire()

        try:
            self.tasks[key] = task
        finally:
            self.lock.release()

    def remove_task(self, key):
        self.lock.acquire()

        try:
            del self.tasks[key]
        finally:
            self.lock.release()

    def is_task_active(self, key):
        if key not in self.tasks:
            return False

        return self.tasks[key]

    def is_working(self):
        tasks_in_progress = any(self.tasks)

        return tasks_in_progress

