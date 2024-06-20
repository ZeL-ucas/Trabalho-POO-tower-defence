import pygame
from Src.Utils import constants
from Src.Entities.tower import Tower
from Utils.towerData import towerDamage
from Utils.functions import loadAnimation


class TowerDamage(Tower):
    def __init__(self, posX: int, posY: int) -> None:
        image = pygame.image.load("Assets/Sprites/Towers/TowerDamage/towerDamage.png").convert_alpha()
        super().__init__(image, posX, posY)
        self.projectile_image_ = pygame.transform.scale(pygame.image.load("Assets/Sprites/Projectiles/TowerDamage/damage_projectile.png").convert_alpha(), (150, 150))
        self.sprite_sheet = pygame.image.load("Assets/Sprites/Towers/TowerDamage/towerDamageTop.png").convert_alpha()
        self.animation_list = loadAnimation(self.sprite_sheet, self.frames)
        self.range_ = towerDamage[self.upgrade_level_ - 1].get("range")
        self.damage_ = towerDamage[self.upgrade_level_ -1].get("damage")
        self.attackCD_ = towerDamage[self.upgrade_level_ - 1].get("cooldown")
        self.upcost_ = towerDamage[self.upgrade_level_ - 1].get("upcost")
        self.price = constants.priceDamage
    def upgrade(self)->None:
        self.upgrade_level_ += 1
        self.range_ = towerDamage[self.upgrade_level_ - 1].get("range")
        self.damage_ = towerDamage[self.upgrade_level_ -1].get("damage")
        self.attackCD_ = towerDamage[self.upgrade_level_ - 1].get("cooldown")
        self.upcost_ = towerDamage[self.upgrade_level_ - 1].get("upcost")
