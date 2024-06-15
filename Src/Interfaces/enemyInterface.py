from abc import ABC,abstractmethod

class InterfaceEnemy(ABC):
    @abstractmethod
    def update(self)->None:
        """
        Atualiza o estado do inimigo.
        """
        pass
    @abstractmethod
    def move(self)->None:
        """
        Move o inimigo para o próximo waypoint.
        """
        pass
    @abstractmethod
    def rotate(self)->None:
        """
        Rotaciona o inimigo para ficar de frente para o próximo waypoint.
        """
        pass
    @abstractmethod
    def takeDamage(self)->None:
        """
        Aplica dano ao inimigo.
        """
        pass
    @abstractmethod
    def kill(self)->None:
        """
        Mata o inimigo. 
        """
        pass
    @abstractmethod
    def getMaxHealth(self)->int:
        """
        Retorna a vida máxima do inimigo.
        """
        pass