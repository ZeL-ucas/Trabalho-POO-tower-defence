from abc import ABC, abstractmethod

class InterfaceTower(ABC):
    @abstractmethod
    def update(self)->None:
        pass
    
    @abstractmethod
    def getTargetEnemy(self)->None:
        pass

    @abstractmethod
    def getTargetEnemy(self):
        pass

    @abstractmethod
    def isWithinRange(self)->float:
        pass

    @abstractmethod
    def calculateDistance(self)->float:
        pass

    @abstractmethod
    def attack(self)->None:
        pass

    @abstractmethod
    def drawRange(self)->None:
        pass

    @abstractmethod
    def zapper(self)->None:
        pass
    
    @abstractmethod
    def getPosition(self)->tuple:
        pass

    @abstractmethod
    def upgrade(self)->None:
        pass
    
    @staticmethod
    @abstractmethod
    def drawRays():
        pass