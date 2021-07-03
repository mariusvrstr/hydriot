import asyncio

from tasks.contracts.base_task import BaseTask
from utilities.dependency_injection import Container
from settings.trigger_config import TriggerConfig
from utilities.dependency_injection import Container

class NutrientDoseTask(BaseTask):

    def run_custom(self):
        print(f"starting example task [NutrientDoseTask]")

        nutrient_trigger = Container().nutrient_relay_factory()
        ## nutrient_trigger.set_tds_sensor_summary(tds_summary)
        dose_duration_seconds = TriggerConfig().get_tds_dose_time_seconds()

        asyncio.run(nutrient_trigger.dose(dose_duration_seconds))

        self.finished.emit()