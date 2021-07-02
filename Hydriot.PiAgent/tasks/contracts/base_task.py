from PyQt5.QtCore import QObject, pyqtSignal

class BaseTask(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    
    async def run(self): raise Exception(f"Not implimented for [{self.__name__}]")