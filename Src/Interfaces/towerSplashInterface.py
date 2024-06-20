from abc import ABC,abstractmethod
class InterfaceTowerSplash(ABC):
    @abstractmethod
    def update(self)->None:
        pass

    @abstractmethod
    def attack(self)->None:
        pass
