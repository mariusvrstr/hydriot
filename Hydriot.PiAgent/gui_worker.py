from time import sleep

from PyQt5.QtCore import QThread
from utilities.thread_wrapper import ThreadWrapper
from tasks.nutrient_dose_task import NutrientDoseTask
from tasks.ph_down_dose_task import PhDownTask
from tasks.read_sensors_task import ReadSensorsTask
from common.task_manager import TaskManager

class GuiWorker:
    task_manager = None
    _threads = dict()           # Keep from garbage collection

    def __init__(self, task_manager = TaskManager()) -> None:       
        self.task_manager = task_manager
    
    def action_start_sensors(self, button, label):
        self.execute_task(ReadSensorsTask(), button, label)  

    def action_ph_down_dose(self, button, label):
        self.execute_task(PhDownTask(), button, label)        

    def action_nutrient_dose(self, button, label):
        self.execute_task(NutrientDoseTask(), button, label)
   
    def execute_task(self, task, button, label):
        job_type = type(task).__name__

        if not self.task_manager.is_task_active(job_type):
            self._threads[job_type] = QThread()
        
        wrapper = ThreadWrapper(self.task_manager, task, button, label)
        wrapper.run_task(self._threads[job_type])

