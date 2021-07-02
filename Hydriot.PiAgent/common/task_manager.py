import threading

class TaskManager():
    tasks = dict()
    lock = None

    def __init__(self) -> None:
        self.lock =  threading.Lock()

    def add_task(self, task):
        task_type = type(task).__name__

        self.lock.acquire()

        try:
            if task_type in self.tasks:
                raise Exception(f"Cannot add task [{task_type}] one is already existing.")
            self.tasks[task_type] = task
        finally:
            self.lock.release()

    def add__update_task(self, task):
        task_type = type(task).__name__
        self.lock.acquire()

        try:
            self.tasks[task_type] = task
        finally:
            self.lock.release()

    def remove_task(self, task):
        task_type = type(task).__name__
        self.lock.acquire()

        try:
            del self.tasks[task_type]
        finally:
            self.lock.release()

    def is_task_active(self, task):
        task_type = type(task).__name__

        if task_type not in self.tasks:
            return False

        return self.tasks[task_type]

    def is_working(self):
        tasks_in_progress = any(self.tasks)

        return tasks_in_progress

