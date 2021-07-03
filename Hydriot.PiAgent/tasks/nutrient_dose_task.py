import time

from tasks.contracts.base_task import BaseTask

class NutrientDoseTask(BaseTask):

    def run_custom(self):
        print(f"starting example task [NutrientDoseTask]")
        
        for i in range(5, 0, -1):
            print(f"Tic [{i}]")
            time.sleep(1)

    