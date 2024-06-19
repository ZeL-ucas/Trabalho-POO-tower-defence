from abc import ABC,abstractmethod


class InterfaceTowerMenu(ABC):

    @abstractmethod
    def draw(self) -> None:
        pass

    @abstractmethod
    def is_clicked(self)->str:
        pass
