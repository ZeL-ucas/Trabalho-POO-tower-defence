import pygame
from Src.Utils import constants
from Src.Entities.tower import Tower
from Utils.towerData import towerSlow
from Utils.functions import loadAnimation


class TowerSlow(Tower):
    def __init__(self, posX: int, posY: int) -> None:
        image = pygame.image.load("Assets/Sprites/Towers/TowerSlow/towerSlow.png").convert_alpha()
        super().__init__(image, posX, posY)
        self.projectile_image_ = pygame.image.load("Assets/Sprites/Projectiles/TowerSlow/damage_projectile.png").convert_alpha()
        self.sprite_sheet = pygame.image.load("Assets/Sprites/Towers/TowerSlow/towerSlowTop.png").convert_alpha()
        self.animation_list = loadAnimation(self.sprite_sheet, self.frames)
        self.range_ = towerSlow[self.upgrade_level_ - 1].get("range")
        self.damage_ = towerSlow[self.upgrade_level_ -1].get("damage")
        self.attackCD_ = towerSlow[self.upgrade_level_ - 1].get("cooldown")
        self.upcost_ = towerSlow[self.upgrade_level_ - 1].get("upcost")
        self.price = constants.priceSlow
        self.slow = True
        