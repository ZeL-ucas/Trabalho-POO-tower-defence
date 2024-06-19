from abc import ABC,abstractmethod

class InterfaceEndMenu(ABC):
    @abstractmethod
    def drawText(self) -> None:
        pass
    
    @abstractmethod
    def drawButton(self)->None:
        pass

    @abstractmethod
    def draw(self)->None:
        pass

    @abstractmethod
    def run(self)->None:
        pass