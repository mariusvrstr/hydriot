"""
============================================================
=== This is the main executable file for the application ===
============================================================
"""

import sys

from PyQt5.QtCore import Qt, QThread
from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget)
from background_worker import BackgroundWorker
from settings.app_config import AppConfig
from settings.trigger_config import TriggerConfig
from gui_worker import GuiWorker

class Window(QMainWindow):

    hydriot = None
    tds_sensor = None
    water_level_sensor = None
    voltage_tester = None    
    light_trigger = None
    water_pump_trigger = None
    sensors = []
    gui_worker = None

    def __init__(self):
        super().__init__(parent = None)
        AppConfig()
        TriggerConfig()
        self.gui_worker = GuiWorker()
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
        self.nutrient_button.setEnabled(False)
        self.nutrient_label.setText(f"Starting nutrient dosage...")
        self.gui_worker.action_nutrient_dose(self.nutrient_button, self.nutrient_label) 
        ## self.nutrient_button.setEnabled(True)   

    def dose_ph_down(self):
        self.ph_down_button.setEnabled(False)
        self.ph_down_label.setText(f"Starting Ph Down dosage...")
        self.gui_worker.action_ph_down_dose(self.ph_down_button, self.ph_down_label) ## self.get_ph_sensor(),
        ## self.ph_down_button.setEnabled(True)

    def reportProgress(self, counter):
        output = self.update_sensors(counter)
        self.sensors_label.setText(f"Available Sensors >> {output}")

    def runLongTask(self):
        self.background_thread = QThread()
        self.background_worker = BackgroundWorker()

        self.background_worker.moveToThread(self.background_thread)

        self.background_thread.started.connect(self.background_worker.run)
        self.background_worker.finished.connect(self.background_thread.quit)
        self.background_worker.finished.connect(self.background_worker.deleteLater)
        self.background_thread.finished.connect(self.background_thread.deleteLater)
        self.background_worker.progress.connect(self.reportProgress)

        self.background_thread.start()

        self.sensors_button.setEnabled(False)

        self.background_thread.finished.connect(
            lambda: self.sensors_button.setEnabled(True)
        )
        self.background_thread.finished.connect(
            lambda: self.sensors_label.setText("Sensors stopped.")
        )

app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec())

