from time import sleep
from utilities.dependency_injection import Container
from settings.trigger_config import TriggerConfig
from utilities.dependency_injection import Container
from utilities.thread_wrapper import ThreadWrapper
from tasks.nutrient_dose_task import NutrientDoseTask
from tasks.ph_down_dose_task import PhDownDoseTask
from common.task_manager import TaskManager

import asyncio

class GuiWorker:
    thread_wrapper = None
    nutrient_task = None
    ph_down_task = None
    task_manager = None
    loop = None
    do_once = True

    def __init__(self) -> None:
        self.task_manager = TaskManager()
        
        self.thread_wrapper = ThreadWrapper(self.task_manager)
        self.nutrient_task = NutrientDoseTask()
        self.ph_down_task = PhDownDoseTask()
        self.task_manager = TaskManager()
        self.loop = asyncio.new_event_loop()        
        asyncio.set_event_loop(self.loop)

    ## This needs to be running on a different thread than the UX to ensure it stays non-blocking
    async def run_container(self):
        counter = 0

        while self.task_manager.is_working():
            counter += 1

            await asyncio.sleep(1)   
            print(f"Keep alive tic [{counter}]")

    def ensure_container_is_running(self):
        if not self.task_manager.is_working():
            self.loop.run_until_complete(self.run_container())

    ## What is causing the UI locks? Asyncio run until complete? Can tasks be injected while running?
    def action_ph_down_dose(self, ph_down_summary):
        self.loop.create_task(self.thread_wrapper.run_task(self.ph_down_task)) 
        self.ensure_container_is_running()        

        ## ph_down_trigger = Container().ph_down_relay_factory()
        ## ph_down_trigger.set_ph_down_sensor_summary(ph_down_summary)
        ## dose_duration_seconds = TriggerConfig().get_ph_down_dose_time_seconds()

        ## asyncio.run(ph_down_trigger.dose(dose_duration_seconds))

    def  action_nutrient_dose(self, tds_summary):
        self.loop.create_task(self.thread_wrapper.run_task(self.nutrient_task)) 
        self.ensure_container_is_running()
        
        ## nutrient_trigger = Container().nutrient_relay_factory()
        ## nutrient_trigger.set_tds_sensor_summary(tds_summary)
        ## dose_duration_seconds = TriggerConfig().get_tds_dose_time_seconds()

        ## asyncio.run(nutrient_trigger.dose(dose_duration_seconds))

