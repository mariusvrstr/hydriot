
class ThreadWrapper:
    task_name = None
    task_manager = None
    current_task = None
    button = None
    label = None

    def __init__(self, task_manager, current_task, button, label) -> None:
        self.task_manager = task_manager
        self.current_task = current_task
        self.button = button
        self.label = label
        self.task_name = type(current_task).__name__

    def report_progress(self, int_value):
        print(f"Report [{int_value}]")
   
    def run_task(self, thread):
        self.task_manager.add_task(self.task_name, self.current_task) ##TODO: Add debug point for self.cleanup to run (else it does not trigger)

        self.current_task.moveToThread(thread)

        thread.started.connect(self.current_task.run)
        self.current_task.finished.connect(thread.quit)
        self.current_task.finished.connect(self.current_task.deleteLater)        
        thread.finished.connect(thread.deleteLater)
 
        thread.start()
        return thread
      