from abc import ABC,abstractmethod

class InterfaceHealer(ABC):
    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def healNearbyEnemies(self)->None:
        """
        Chama o método "update" da classe "Enemy" para atualizar o estado padrão do inimigo. 
        Além disso, verifica se o tempo atual menos o tempo da última cura é maior ou igual 
        ao intervalo de cura, e se sim, cura inimigos próximos e atualiza o tempo da última cura.
        """
        pass
    @abstractmethod
    def applyHeal(self)->None:
        """
        Verifica se há inimigos próximos dentro do raio de cura para aplicar a cura a eles.
        """
        pass
