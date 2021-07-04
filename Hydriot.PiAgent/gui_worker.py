from time import sleep

from PyQt5.QtCore import QThread
from utilities.thread_wrapper import ThreadWrapper
from tasks.nutrient_dose_task import NutrientDoseTask
from tasks.ph_down_dose_task import PhDownTask
from tasks.read_sensors_task import ReadSensorsTask
from common.task_manager import TaskManager

class TaskGroup:
    button = None
    label = None    
    task_name = None
    task = None

    def __init__(self, task, button, label) -> None:
        self.button = button
        self.label = label
        self.task = task
        self.task_name = type(task).__name__

class GuiWorker:
    task_manager = None
    _threads = dict()           # Keep from garbage collection
    sensors = []

    sensor_group = None
    ph_down_dose_group = None
    nutrient_dose_group = None

    def cleanup_sensors(self):
        self.cleanup(self.sensor_group)

    def cleanup_ph_down(self):
        self.cleanup(self.ph_down_dose_group)

    def cleanup_nutrient(self):
        self.cleanup(self.nutrient_dose_group)

    def __init__(self, task_manager = TaskManager()) -> None:       
        self.task_manager = task_manager

    def action_start_sensors(self, button, label):
        self.sensor_group = TaskGroup(ReadSensorsTask(), button, label)
        self.sensor_group.task.progress.connect(self.sensor_feedback_update)
        self.sensor_group.task.finished.connect(self.cleanup_sensors)
        self.execute_task(self.sensor_group.task, button, label)

    def action_ph_down_dose(self, button, label):
        self.ph_down_dose_group = TaskGroup(PhDownTask(), button, label)
        self.ph_down_dose_group.task.finished.connect(self.cleanup_ph_down)
        self.execute_task(self.ph_down_dose_group.task, button, label)

    def action_nutrient_dose(self, button, label):
        self.nutrient_dose_group = TaskGroup(NutrientDoseTask(), button, label)
        self.nutrient_dose_group.task.finished.connect(self.cleanup_nutrient)
        self.execute_task(self.nutrient_dose_group.task, button, label)
   
    def execute_task(self, task, button, label):
        job_type = type(task).__name__

        if not self.task_manager.is_task_active(job_type):
            self._threads[job_type] = QThread()
        
        wrapper = ThreadWrapper(self.task_manager, task, button, label)
        wrapper.run_task(self._threads[job_type])

    def cleanup(self, group):
        group.button.setEnabled(True)
        group.label.setText(f"Completed [{group.task_name}]")
        self.task_manager.remove_task(group.task_name)

    def sensor_feedback_update(self, sensor):
        char_limit = 10
        delimiter = "|"
        found = False

        for k in range(len(self.sensors)):
            if sensor.name == self.sensors[k].name:
                self.sensors[k] = sensor
                found = True

        if not found:
            self.sensors.append(sensor)

        sensor_list = ""
        for sensor in self.sensors:
            if len(sensor.name) <= char_limit:
                sensor_list += f"{sensor.name}{delimiter} "
                continue

            sensor_list += f"{sensor.name[0:char_limit]}..{delimiter} "            

        self.sensor_group.label.setText(f"Sensors: {sensor_list[0:len(sensor_list)-2]}")
    

