"""
============================================================
=== This is the main executable file for the application ===
============================================================
"""

import sys
import asyncio

from PyQt5.QtCore import Qt, QThread
from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget)
from background_worker import BackgroundWorker
from settings.app_config import AppConfig
from settings.trigger_config import TriggerConfig
from utilities.dependency_injection import Container

class Window(QMainWindow):

    hydriot = None
    tds_sensor = None
    water_level_sensor = None
    voltage_tester = None    
    light_trigger = None
    water_pump_trigger = None
    sensors = []

    def __init__(self):
        super().__init__(parent = None)
        AppConfig()
        TriggerConfig()
        self.setupUi()

    def get_tds_sensor(self):
        for sensor in self.sensors:
            if "tds" in sensor.name.lower():
                return sensor        
        return None
    
    def get_ph_sensor(self):
        for sensor in self.sensors:
            if "ph" in sensor.name.lower():
                return sensor        
        return None   

    def update_sensors(self, counter):
        found = False

        for k in range(len(self.sensors)):
            if counter.name == self.sensors[k].name:
                self.sensors[k] = counter
                found = True

        if not found:
            self.sensors.append(counter)

        sensor_message = ""
        for sensor in self.sensors:
            sensor_message += f"{sensor.name}, "

        return sensor_message

    def setupUi(self):
        self.setWindowTitle("Hydriot Node")
        self.resize(300, 150)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        # Nutrient Dosage
        self.nutrient_label = QLabel("Nutrient dose on command", self)
        self.nutrient_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.nutrient_button = QPushButton("Nutrient Dosage", self)   
        self.nutrient_button.clicked.connect(self.dose_nutrient)

        # Ph Down Dosage
        self.ph_down_label = QLabel("Ph down dose on command", self)
        self.ph_down_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.ph_down_button = QPushButton("Ph Down Dosage", self)         
        self.ph_down_button.clicked.connect(self.dose_ph_down)

        self.sensors_button = QPushButton("Start Sensors", self)        
        self.sensors_button.clicked.connect(self.runLongTask)
        self.sensors_label = QLabel("Sensor Readings (Background Thread)")

        # Set the layout
        layout = QVBoxLayout()

        layout.addWidget(self.sensors_label)
        layout.addWidget(self.sensors_button)
        
        layout.addStretch()
   
        layout.addWidget(self.nutrient_label)
        layout.addWidget(self.nutrient_button)
        layout.addStretch()

        layout.addWidget(self.ph_down_label)
        layout.addWidget(self.ph_down_button)
        layout.addStretch()        
       
        self.centralWidget.setLayout(layout)

    def dose_nutrient(self):
        nutrient_trigger = Container().nutrient_relay_factory()
        tds_summary = self.get_tds_sensor()
        nutrient_trigger.set_tds_sensor_summary(tds_summary)
        dose_duration_seconds = TriggerConfig().get_tds_dose_time_seconds()

        self.nutrient_label.setText(f"Starting [{dose_duration_seconds}] second nutrient dosage...")
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(nutrient_trigger.dose(dose_duration_seconds))
        self.nutrient_label.setText(f"Nutrient dosage complete.")       

    def dose_ph_down(self):
        ph_down_trigger = Container().ph_down_relay_factory()
        ph_down_summary = self.get_ph_sensor()
        ph_down_trigger.set_ph_down_sensor_summary(ph_down_summary)
        dose_duration_seconds = TriggerConfig().get_ph_down_dose_time_seconds()

        self.ph_down_label.setText(f"Starting [{dose_duration_seconds}] second Ph Down dosage...")
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(ph_down_trigger.dose(dose_duration_seconds))
        self.ph_down_label.setText(f"Ph Down dosage complete.")     

    def reportProgress(self, counter):
        output = self.update_sensors(counter)
        self.sensors_label.setText(f"Available Sensors >> {output}")

    def runLongTask(self):
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = BackgroundWorker()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportProgress)

        # Step 6: Start the thread
        self.thread.start()

        # Final resets
        self.sensors_button.setEnabled(False)

        self.thread.finished.connect(
            lambda: self.sensors_button.setEnabled(True)
        )
        self.thread.finished.connect(
            lambda: self.sensors_label.setText("Sensors stopped.")
        )

app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec())

