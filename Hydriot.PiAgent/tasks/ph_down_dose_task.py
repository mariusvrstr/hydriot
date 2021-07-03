import asyncio

from tasks.contracts.base_task import BaseTask
from utilities.dependency_injection import Container
from settings.trigger_config import TriggerConfig
from utilities.dependency_injection import Container

class PhDownTask(BaseTask):

    def run_custom(self):
        print(f"starting example task [PhDownTask]")

        ph_down_trigger = Container().ph_down_relay_factory()
        ## ph_down_trigger.set_ph_down_sensor_summary(ph_down_summary)
        dose_duration_seconds = TriggerConfig().get_ph_down_dose_time_seconds()

        asyncio.run(ph_down_trigger.dose(dose_duration_seconds))

        self.finished.emit() 
