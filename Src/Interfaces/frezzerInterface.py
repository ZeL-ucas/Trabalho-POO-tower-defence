from abc import ABC,abstractmethod

class InterfaceFrezzer(ABC):
    @abstractmethod
    def kill(self, killed: bool)->None:
        pass
        """
        Define o que acontece quando o Frezzer morre. Se o freezer tiver estiver vivo, ele será
        marcado como morto. Além disso, se ele foi morto por um jogador, ele congela a torre mais 
        próxima chamando freeze_nearest_tower. E, Chama a callback de morte se ela existir e então 
        remove o Frezzer do grupo de sprites.
        """

    @abstractmethod
    def freeze_nearest_tower(self)->None:
        pass
        """
        Encontra e congela a torre mais próxima ao frezzer. Intera pelo grupo de torres, calcula a 
        distância entre cada torre e o Frezzer, e mantém a referência à torre mais próxima.
        """