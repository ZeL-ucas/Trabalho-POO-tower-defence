import pygame
import math
from Src.Utils import constants
from Src.Entities.tower import Tower
from Utils.towerData import towerSlow
from Utils.functions import loadAnimation
from Src.Entities.enemy import Enemy
from Src.Entities.projectiles import Projectile


class TowerSlow(Tower):
    def __init__(self, posX: int, posY: int) -> None:
        image = pygame.image.load("Assets/Sprites/Towers/TowerSlow/towerSlow.png").convert_alpha()
        super().__init__(image, posX, posY)
        self.projectile_image_ = pygame.image.load("Assets/Sprites/Projectiles/TowerSlow/slow_projectile.png").convert_alpha()
        self.sprite_sheet = pygame.image.load("Assets/Sprites/Towers/TowerSlow/towerSlowTop.png").convert_alpha()
        self.animation_list = loadAnimation(self.sprite_sheet, self.frames)
        self.range_ = towerSlow[self.upgrade_level_ - 1].get("range")
        self.damage_ = towerSlow[self.upgrade_level_ -1].get("damage")
        self.attackCD_ = towerSlow[self.upgrade_level_ - 1].get("cooldown")
        self.upcost_ = towerSlow[self.upgrade_level_ - 1].get("upcost")
        self.slowDuration = towerSlow[self.upgrade_level_ -1].get("slowDuration")
        self.slowPotential = towerSlow[self.upgrade_level_ -1].get("slowPotential")
        self.price = constants.priceSlow
        
    def attack(self,enemy: Enemy,projectileGroup: pygame.sprite.Group)->None:
        direction = pygame.math.Vector2(enemy.rect.center) - pygame.math.Vector2(self.rect.center)
        angle_rad = math.atan2(direction.y, direction.x)
        angle_deg = math.degrees(angle_rad) + 180
        rotated_projectile = pygame.transform.rotate(self.projectile_image_, -angle_deg)
        
        adjusted_pos = (self.rect.centerx, self.rect.centery)  
        projectile = Projectile(rotated_projectile, adjusted_pos, enemy, self.damage_)
        projectileGroup.add(projectile)
        enemy.Slow(self.slowDuration, self.slowPotential)

    def upgrade(self)->None:
        self.upgrade_level_ += 1
        self.range_ = towerSlow[self.upgrade_level_ - 1].get("range")
        self.damage_ =towerSlow[self.upgrade_level_ -1].get("damage")
        self.attackCD_ = towerSlow[self.upgrade_level_ - 1].get("cooldown")
        self.upcost_ = towerSlow[self.upgrade_level_ - 1].get("upcost")