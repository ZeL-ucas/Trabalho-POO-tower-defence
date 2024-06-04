from abc import ABC, abstractmethod

class InterfaceTower(ABC):
    @abstractmethod
    def update(self)->None:
        pass
    
    @abstractmethod
    def getTargetEnemy(self)->None:
        pass

    @abstractmethod
    def getTargetEnemy(self)->Enemy:
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
    def freeze(self)->None:
        pass
    
    @abstractmethod
    def get_position(self)->list:
        pass

    @abstractmethod
    def upgrade(self)->None:
        pass
