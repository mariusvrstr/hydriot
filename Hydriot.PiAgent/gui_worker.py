from time import sleep
from utilities.dependency_injection import Container
from settings.trigger_config import TriggerConfig
from utilities.dependency_injection import Container

import asyncio

class GuiWorker:

    def __init__(self) -> None:
        pass

    def action_ph_down_dose(self, ph_down_summary): 
        ph_down_trigger = Container().ph_down_relay_factory()
        ph_down_trigger.set_ph_down_sensor_summary(ph_down_summary)
        dose_duration_seconds = TriggerConfig().get_ph_down_dose_time_seconds()

        asyncio.run(ph_down_trigger.dose(dose_duration_seconds))

    def action_nutrient_dose(self, tds_summary):
        nutrient_trigger = Container().nutrient_relay_factory()
        nutrient_trigger.set_tds_sensor_summary(tds_summary)
        dose_duration_seconds = TriggerConfig().get_tds_dose_time_seconds()

        asyncio.run(nutrient_trigger.dose(dose_duration_seconds))

