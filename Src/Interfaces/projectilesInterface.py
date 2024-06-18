from abc import ABC, abstractmethod

class InterfaceProjectiles(ABC):
    @abstractmethod
    def update(self) -> None:
        
        """
        Calcula a direção e a distância do projétil em relação ao alvo. Além disso, se o projétil
        está próximo o suficiente do alvo (distância <= velocidade), aplica dano ao alvo e remove 
        o projétil. Caso contrário, move o projétil na direção do alvo, normalizando a direção e 
        multiplicando pela velocidade para garantir movimento uniforme.
        """
        pass
