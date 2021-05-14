from abc import ABC, abstractmethod ## abstract module

class DriverBase(ABC):

    def __init__(self):
        self.initialize()
        pass

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def read_value(self): raise NotImplementedError

    @abstractmethod
    def is_available(self): raise NotImplementedError


