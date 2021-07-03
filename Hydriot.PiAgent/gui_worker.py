from time import sleep

from PyQt5.QtCore import QThread
from utilities.thread_wrapper import ThreadWrapper
from tasks.nutrient_dose_task import NutrientDoseTask
from tasks.ph_down_dose_task import PhDownTask
from common.task_manager import TaskManager

class GuiWorker:
    task_manager = None
    _nutrient_thread = None     # Keep from garbage collection
    _ph_thread = None           # Keep from garbage collection

    def __init__(self, task_manager = TaskManager()) -> None:       
        self.task_manager = task_manager

    def action_ph_down_dose(self, button, label):
        task = PhDownTask()

        if not self.task_manager.is_task_active(type(task).__name__):
            self._ph_thread = QThread()
        
        wrapper = ThreadWrapper(self.task_manager, task, button, label)
        wrapper.run_task(self._ph_thread)

    def  action_nutrient_dose(self, button, label):
        task = NutrientDoseTask()

        if not self.task_manager.is_task_active(type(task).__name__):
            self._nutrient_thread = QThread()

        wrapper = ThreadWrapper(self.task_manager, task, button, label)
        wrapper.run_task(self._nutrient_thread)       


