import pygame
from Src.Utils import constants
from Src.Entities.enemy import Enemy

class Tank(Enemy):
    def __init__(self, waypoints: list, death_callback=None) -> None:
        image = pygame.image.load("Assets/Sprites/Enemys/Tank/tank.png").convert_alpha()
        super().__init__(waypoints, constants.ANIMATION_STEPS_ENEMY_TANK, image, "tank", death_callback)
        self.bounty = constants.bountyTank

    """
    Define a lógica básica de um inimigo do tipo Tank, que é um inimigo com alta vida,
    velocidade específica e oferece uma alta recompensa quando derrotado. A funcionalidade 
    principal é herdada da classe Enemy, enquanto os atributos específicos são definidos de 
    acordo com as constantes apropriadas.
    """