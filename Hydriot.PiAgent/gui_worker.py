from time import sleep

from PyQt5.QtCore import QThread
from utilities.dependency_injection import Container
from settings.trigger_config import TriggerConfig
from utilities.dependency_injection import Container
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

        ## ph_down_trigger = Container().ph_down_relay_factory()
        ## ph_down_trigger.set_ph_down_sensor_summary(ph_down_summary)
        ## dose_duration_seconds = TriggerConfig().get_ph_down_dose_time_seconds()

        ## asyncio.run(ph_down_trigger.dose(dose_duration_seconds))

    def  action_nutrient_dose(self, button, label):
        task = NutrientDoseTask()

        if not self.task_manager.is_task_active(type(task).__name__):
            self._nutrient_thread = QThread()

        wrapper = ThreadWrapper(self.task_manager, task, button, label)
        wrapper.run_task(self._nutrient_thread)
        
        ## nutrient_trigger = Container().nutrient_relay_factory()
        ## nutrient_trigger.set_tds_sensor_summary(tds_summary)
        ## dose_duration_seconds = TriggerConfig().get_tds_dose_time_seconds()

        ## asyncio.run(nutrient_trigger.dose(dose_duration_seconds))

