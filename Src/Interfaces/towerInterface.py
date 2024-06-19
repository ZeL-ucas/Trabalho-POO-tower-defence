from abc import ABC, abstractmethod
from Entities.enemy import Enemy
class InterfaceTower(ABC):
    @abstractmethod
    def update(self)->None:
        pass
    
    @abstractmethod
    def getTargetEnemy(self)->Enemy:
        pass


    @abstractmethod
    def isWithinRange(self)->bool:
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