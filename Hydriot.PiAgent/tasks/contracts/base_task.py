from PyQt5.QtCore import QObject, pyqtSignal

class BaseTask(QObject):
    finished = pyqtSignal()

    def run_custom(self):
        raise Exception(f"Not implimented for [{self.__name__}]")
    
    def run(self):
        self.run_custom()