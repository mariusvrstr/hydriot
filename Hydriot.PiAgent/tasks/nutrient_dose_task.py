import time

from tasks.contracts.base_task import BaseTask

class NutrientDoseTask(BaseTask):

    def run(self):
        print(f"starting example task [NutrientDoseTask]")
        time.sleep(3)
