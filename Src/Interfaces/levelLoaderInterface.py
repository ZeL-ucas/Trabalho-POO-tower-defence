from abc import ABC, abstractmethod

class InterfaceLevelLoader(ABC):
    @abstractmethod
    def ProcessData(self)->None:
        pass

    @abstractmethod
    def loadWaves(self)->list:
        pass

    @abstractmethod
    def draw(self)->None:
        pass