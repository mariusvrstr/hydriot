import time

from tasks.contracts.base_task import BaseTask

class PhDownTask(BaseTask):

    def run(self):
        print(f"starting example task [PhDownTask]")
        time.sleep(3)