import pygame
from Src.Utils import functions
from Src.Utils import constants
from Src.Entities.enemy import Enemy

class Tank(Enemy):
    def __init__(self, waypoints, death_callback=None) -> None:
        image = pygame.image.load("Assets/Sprites/Enemys/Tank/tank.png").convert_alpha()
        super().__init__(waypoints,11, image, death_callback)
        self.health_= constants.tankHealth
        self.speed = constants.tankSpeed
        self.lifes =constants.tankLifes
        self.bounty = 200