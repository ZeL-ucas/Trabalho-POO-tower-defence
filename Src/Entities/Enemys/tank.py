import pygame
from Src.Utils import functions
from Src.Utils import constants
from Src.Entities.enemy import Enemy

class Tank(Enemy):
    def __init__(self, waypoints, death_callback=None) -> None:
        image = "Assets/Sprites/Enemys/Tank/tank.png"
        sprites = functions.load_sprite_sheet(image,9,8)
        self.enemyImage_ = pygame.image.load(image).convert_alpha()
        self.enemyImage_ = pygame.transform.scale(self.enemyImage_, (48, 48))
        super().__init__(waypoints, self.enemyImage_, death_callback)
        self.frames = 12
        self.animation_list = self.load_images(self.frames)
        self.health_= constants.tankHealth
        self.speed = constants.tankSpeed
        self.lifes =constants.tankLifes
        self.bounty = 200