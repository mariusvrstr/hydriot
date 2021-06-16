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
        # Create and connect widgets
        self.clicksLabel = QLabel("Dose on command", self)
        self.clicksLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.stepLabel = QLabel("Sensor Readings (Background Thread)")
        self.stepLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.countBtn = QPushButton("Nutrient Dosage", self)
        self.countBtn.clicked.connect(self.dose_nutrient)
        self.longRunningBtn = QPushButton("Start Sensors", self)
        self.longRunningBtn.clicked.connect(self.runLongTask)
        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.clicksLabel)
        layout.addWidget(self.countBtn)
        layout.addStretch()
        layout.addWidget(self.stepLabel)
        layout.addWidget(self.longRunningBtn)
        self.centralWidget.setLayout(layout)

    def dose_nutrient(self):
        nutrient_trigger = Container().nutrient_relay_factory()
        tds_summary = self.get_tds_sensor()
        nutrient_trigger.set_tds_sensor_summary(tds_summary)
        dose_duration_seconds = TriggerConfig().get_dose_time_seconds()

        self.clicksLabel.setText(f"Starting [{dose_duration_seconds}] second nutrient dosage...")
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(nutrient_trigger.dose(dose_duration_seconds))
        self.clicksLabel.setText(f"Nutrient dosage complete.")       

    def reportProgress(self, counter):
        output = self.update_sensors(counter)
        self.stepLabel.setText(f"Long-Running Step: {output}")

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
        self.longRunningBtn.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.longRunningBtn.setEnabled(True)
        )
        self.thread.finished.connect(
            lambda: self.stepLabel.setText("Long-Running Step: 0")
        )

app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec())

