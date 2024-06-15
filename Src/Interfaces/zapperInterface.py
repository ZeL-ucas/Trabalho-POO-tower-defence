from abc import ABC,abstractmethod

class InterfaceZapper(ABC):
    @abstractmethod
    def kill(self, killed: bool)->None:
        pass
        """
        Define o que acontece quando o Zapper morre. Se o zapperr tiver estiver vivo, ele será
        marcado como morto. Além disso, se ele foi morto por um jogador, ele congela a torre mais 
        próxima chamando zapper_nearest_tower. E, Chama a callback de morte se ela existir e então 
        remove o Zapper do grupo de sprites.
        """

    @abstractmethod
    def zapper_nearest_tower(self)->None:
        pass
        """
        Encontra e congela a torre mais próxima ao zapper. Intera pelo grupo de torres, calcula a 
        distância entre cada torre e o Zapper, e mantém a referência à torre mais próxima.
        """