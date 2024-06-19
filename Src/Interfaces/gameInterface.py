from abc import ABC,abstractmethod
from Entities.tower import Tower
from Entities.enemy import Enemy
from Entities.Enemys.healer import Healer
from Entities.Enemys.tank import Tank
from Entities.Enemys.zapper import Zapper



class InterfaceGame(ABC):


    @abstractmethod
    def Run(self)->int:
        pass

    @abstractmethod
    def Quit(self) -> None:
        pass

    @abstractmethod
    def Draw(self) -> None:
        pass

    @abstractmethod 
    def CreateTurret(self, pos:tuple) -> None:
        pass

    @abstractmethod
    def CheckSpace(self, pos:tuple) -> int:
        pass

    @abstractmethod
    def menuTower(self, tower:Tower) -> None:
        pass

    @abstractmethod
    def EnemyDied(self, bounty:int,killed:bool,lifes:int)->None:
        pass
        

    @abstractmethod
    def Waves(self)->None:
        pass

    @abstractmethod
    def SpawnEnemy(self, enemy_type:str)->None:
        pass

    @abstractmethod
    def CreateClassicEnemy(self)->Enemy:
        pass

    @abstractmethod
    def CreateHealerEnemy(self)->Healer:
        pass

    @abstractmethod
    def CreateTankEnemy(self)->Tank:
        pass

    @abstractmethod
    def CreateZapperEnemy(self)->Zapper:
        pass

    @abstractmethod
    def Update(self)->None:
        pass

        
    @abstractmethod
    def isClickOutsideMenu(self) -> bool:
        pass

    @abstractmethod
    def UpgradeTower(self) -> None:
        pass

