from PyQt5.QtCore import pyqtSignal, pyqtSignal
from PyQt5.QtCore import QThread

## Single UX Worker Thread with multiple async tasksthat can be added with a group locking of dependant ones
class ThreadWrapper:
    current_thread = None
    task_manager = None
    progress = pyqtSignal(int)

    def __init__(self, task_manager, current_thread = QThread()) -> None:
        self.current_thread = current_thread
        self.task_manager = task_manager

    def report_progress(int_value):
        print(f"Report [{int_value}]")
        pass
    
    def run_task(self, task, button, label):

        self.task_manager.add_task(task)
        task.moveToThread(self.current_thread)
        self.current_thread.started.connect(task.run)
        task.finished.connect(self.current_thread.quit)

        task.finished.connect(task.deleteLater)
        self.current_thread.finished.connect(self.current_thread.deleteLater)
        task.progress.connect(self.report_progress)

        self.current_thread.start()

        task.finished.connect(
            lambda: button.setEnabled(True)
        )

        task.finished.connect(
            lambda: label.setText(f"Completed [{task.__name__}]")
        )