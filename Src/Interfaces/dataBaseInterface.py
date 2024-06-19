
from abc import ABC,abstractmethod
class InterfaceDataBase(ABC):

    @abstractmethod
    def ReadHighScores(self)->list:
        pass

    @abstractmethod
    def GetHighScores(self)->list:
        pass

    @abstractmethod
    def AddHighScore(self, newName:str, newScore:int)->None:
        pass