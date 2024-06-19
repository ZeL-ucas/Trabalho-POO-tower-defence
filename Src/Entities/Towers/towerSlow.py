import pygame
from Src.Utils import constants
from Src.Entities.tower import Tower
from Utils.towerData import towerSlow
from Utils.functions import loadAnimation
from Src.Entities.enemy import Enemy

class TowerSlow(Tower):
    def __init__(self, posX: int, posY: int) -> None:
        image = pygame.image.load("Assets/Sprites/Towers/TowerDamage/towerDamage.png").convert_alpha()
        super().__init__(image, posX, posY)
        self.projectile_image_ = pygame.image.load("Assets/Sprites/Projectiles/TowerDamage/damage_projectile.png").convert_alpha()
        self.sprite_sheet = pygame.image.load("Assets/Sprites/Towers/TowerDamage/towerDamageTop.png").convert_alpha()
        self.animation_list = loadAnimation(self.sprite_sheet, self.frames)
        self.range_ = towerSlow[self.upgrade_level_ - 1].get("range")
        self.damage_ = towerSlow[self.upgrade_level_ -1].get("damage")
        self.attackCD_ = towerSlow[self.upgrade_level_ - 1].get("cooldown")
        self.upcost_ = towerSlow[self.upgrade_level_ - 1].get("upcost")
        self.slowDuration = towerSlow[self.upgrade_level_ -1].get("slowDuration")
        self.slowPotential = towerSlow[self.upgrade_level_ -1].get("slowPotential")
        self.price = constants.priceSlow
        
    def attack(self, enemy:Enemy,additional_param=None) -> None:
        enemy.takeDamage(self.damage_)
        enemy.Slow(self.slowDuration, self.slowPotential)

    def upgrade(self)->None:
        self.upgrade_level_ += 1
        self.range_ = towerSlow[self.upgrade_level_ - 1].get("range")
        self.damage_ =towerSlow[self.upgrade_level_ -1].get("damage")
        self.attackCD_ = towerSlow[self.upgrade_level_ - 1].get("cooldown")
        self.upcost_ = towerSlow[self.upgrade_level_ - 1].get("upcost")