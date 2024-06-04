from abc import ABC,abstractmethod

class InterfaceEnemy(ABC):
    @abstractmethod
    def update(self)->None:
        pass
        """
        Atualiza o estado do inimigo.
        """
    @abstractmethod
    def move(self)->None:
        pass
        """
        Move o inimigo para o próximo waypoint.
        """
    @abstractmethod
    def rotate(self)->None:
        pass
        """
        Rotaciona o inimigo para ficar de frente para o próximo waypoint.
        """
    @abstractmethod
    def take_damage(self)->None:
        pass
        """
        Aplica dano ao inimigo.
        """
    @abstractmethod
    def kill(self)->None:
        pass
        """
        Mata o inimigo. 
        """
    @abstractmethod
    def get_max_health(self)->int:
        pass
        """
        Retorna a vida máxima do inimigo.
        """