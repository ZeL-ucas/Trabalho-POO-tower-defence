from abc import ABC,abstractmethod

class InterfaceHealer(ABC):
    @abstractmethod
    def heal_nearby_enemies(self)->None:
        pass
        """
        Chama o método "update" da classe "Enemy" para atualizar o estado padrão do inimigo. 
        Além disso, verifica se o tempo atual menos o tempo da última cura é maior ou igual 
        ao intervalo de cura, e se sim, cura inimigos próximos e atualiza o tempo da última cura.
        """
    @abstractmethod
    def apply_heal(self,enemy)->None:
        pass
        """
        Verifica se há inimigos próximos dentro do raio de cura para aplicar a cura a eles.
        """
