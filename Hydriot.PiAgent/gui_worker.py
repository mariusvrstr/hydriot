from time import sleep
from utilities.dependency_injection import Container
from settings.trigger_config import TriggerConfig
from utilities.dependency_injection import Container
from utilities.thread_wrapper import ThreadWrapper
from tasks.nutrient_dose_task import NutrientDoseTask
from tasks.ph_down_dose_task import PhDownTask
from common.task_manager import TaskManager

class GuiWorker:
    thread_wrapper = None
    nutrient_task = None
    ph_down_task = None
    task_manager = None

    def __init__(self) -> None:
        self.task_manager = TaskManager()
        
        self.thread_wrapper = ThreadWrapper(self.task_manager)
        self.nutrient_task = NutrientDoseTask()
        self.ph_down_task = PhDownTask()

    ## What is causing the UI locks? Asyncio run until complete? Can tasks be injected while running?
    def action_ph_down_dose(self, button, label):
        self.thread_wrapper.run_task(self.ph_down_task, button, label)

        ## ph_down_trigger = Container().ph_down_relay_factory()
        ## ph_down_trigger.set_ph_down_sensor_summary(ph_down_summary)
        ## dose_duration_seconds = TriggerConfig().get_ph_down_dose_time_seconds()

        ## asyncio.run(ph_down_trigger.dose(dose_duration_seconds))

    def  action_nutrient_dose(self, button, label):
        self.thread_wrapper.run_task(self.nutrient_task, button, label)
        
        ## nutrient_trigger = Container().nutrient_relay_factory()
        ## nutrient_trigger.set_tds_sensor_summary(tds_summary)
        ## dose_duration_seconds = TriggerConfig().get_tds_dose_time_seconds()

        ## asyncio.run(nutrient_trigger.dose(dose_duration_seconds))

