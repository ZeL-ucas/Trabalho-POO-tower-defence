from abc import ABC,abstractmethod

class startMenuInterface(ABC):
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
    def drawInputBox(self)->None:
        pass

    @abstractmethod
    def drawScores(self)->None:
        pass
    @abstractmethod
    def run(self)->None:
        pass