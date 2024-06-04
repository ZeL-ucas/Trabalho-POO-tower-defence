from abc import ABC,abstractmethod

class InterfaceHealer(ABC):
    @abstractmethod
    def heal_nearby_enemies(self)->None:
        pass
    @abstractmethod
    def apply_heal(self,enemy)->None:
        pass
