import pygame
from Src.Utils import functions
from Src.Utils import constants
from Src.Entities.enemy import Enemy

class Tank(Enemy):
    def __init__(self, waypoints, death_callback=None) -> None:
        image = "Assets/Sprites/Enemys/Scorpion.png"
        sprites = functions.load_sprite_sheet(image,9,8)
        self.static = sprites[0][0]
        super().__init__(waypoints, self.static, death_callback)
        self.health_= constants.tankHealth
        self.speed = constants.tankSpeed
        self.lifes =constants.tankLifes
        self.bounty = 200