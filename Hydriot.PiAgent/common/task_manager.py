
class TaskManager:
    tasks = dict()

    def add_task(self, task_key):
        self.tasks[task_key] = True

    def remove_task(self, task_key):
        del self.tasks[task_key]

    def is_task_active(self, task_key):
        if task_key not in self.tasks:
            return False

        return self.tasks[task_key]

    def is_working(self):
        for key in self.tasks:
            if self.tasks[key] == True:
                return True

        return False