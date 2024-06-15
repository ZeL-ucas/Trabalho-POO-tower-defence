from abc import ABC,abstractmethod

class sideMenuInterface(ABC):
    @abstractmethod
    def draw(self) -> None:
        pass