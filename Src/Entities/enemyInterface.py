from abc import ABC,abstractmethod

def InterfaceEnemy(ABC):
    @abstractmethod
    def update(self)->None:
        pass
    @abstractmethod
    def move(self)->None:
        pass
    @abstractmethod
    def rotate(self)->None:
        pass
    @abstractmethod
    def take_damage(self)->None:
        pass
    @abstractmethod
    def kill(self)->None:
        pass
    @abstractmethod
    def get_max_health(self)->int:
        pass