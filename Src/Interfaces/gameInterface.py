from abc import ABC,abstractmethod
from Entities.tower import Tower
from Entities.enemy import Enemy
from Entities.Enemys.healer import Healer
from Entities.Enemys.tank import Tank
from Entities.Enemys.zapper import Zapper



class InterfaceGame(ABC):

    @abstractmethod
    def Run(self)->int:
        """
        Metodo que faz o jogo rodar
        """
        pass

    @abstractmethod
    def Quit(self) -> None:
        """
        Encerra o Pygame e fecha o jogo.
        """
        pass

    @abstractmethod
    def Draw(self) -> None:
        """
        Desenha todos os elementos do jogo na tela.
        """
        pass

    @abstractmethod 
    def CreateTurret(self, pos:tuple) -> None:
        """
        Cria uma torre na posição especificada se o jogador tiver ouro suficiente.
        
        Observação: A variável "pos" é a coordenada X,Y. 
        """
        pass

    @abstractmethod
    def CheckSpace(self, pos:tuple) -> int:
        """
        Verifica se o espaço especificado está disponível para colocar uma torre.
        Retorna:
            1 se o espaço já está ocupado por uma torre.
            2 se o espaço está disponível.
            0 se o espaço não é válido.
        """
        pass

    @abstractmethod
    def menuTower(self, tower:Tower) -> None:
        """
        Mostra o menu de upgrade para a torre especificada.
        """
        pass

    @abstractmethod
    def EnemyDied(self, bounty:int,killed:bool,lifes:int)->None:
        """
        Verifica se o inimigo morreu ou não. Além de retornar o dinheiro obtido ou descontar das vidas do player
        """
        pass
        

    @abstractmethod
    def Waves(self)->None:
        """
        Faz controle das waves e também interagindo com SpawnEnemy
        """
        pass

    @abstractmethod
    def SpawnEnemy(self, enemy_type:str)->None:
        """
        Controla o Spawn de inimigos
        """
        pass

    @abstractmethod
    def CreateClassicEnemy(self)->Enemy:
        """
        Cria inimigo do tipo Classic
        """
        pass

    @abstractmethod
    def CreateHealerEnemy(self)->Healer:
        """
        Cria inimigo do tipo Healer
        """
        pass

    @abstractmethod
    def CreateTankEnemy(self)->Tank:
        """
        Cria inimigo do tipo Tank
        """
        pass

    @abstractmethod
    def CreateZapperEnemy(self)->Zapper:
        """
        Cria inimigo do tipo Zapper
        """
        pass

    @abstractmethod
    def Update(self)->None:
        pass

    @abstractmethod
    def isClickOutsideMenu(self) -> bool:
        """
        Verifica se um clique do mouse está fora do menu de upgrade da torre.
        """
        pass

    @abstractmethod
    def UpgradeTower(self) -> None:
        """
        Realiza o upgrade da torre se o jogador tiver ouro suficiente.
        """
        pass

    @abstractmethod
    def DrawTowerPrices(self) -> None:
        """
        Desenha os preços das torres abaixo dos botões.
        """
        pass