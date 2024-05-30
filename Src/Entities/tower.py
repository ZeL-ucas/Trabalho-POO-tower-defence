from Utils import constants

import pygame
import math
from .projectiles import Projectile
from Utils.towerData import towerData

class Tower(pygame.sprite.Sprite):
    def __init__(self,image,posX, posY) -> None : # colocar no construtor depois mousePosX,mousePosY
        pygame.sprite.Sprite.__init__(self)
        self.posX_ = posX
        self.posY_ = posY
        self.price = 50
        self.X_ = (self.posX_ + 0.5) * constants.tileSize
        self.Y_ = (self.posY_ + 0.2) * constants.tileSize #valor diferente para a torre atual não ficar em cima dos blocos
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.X_, self.Y_)
        self.upgrade_level_ = 1
        self.range_ = towerData[self.upgrade_level_ - 1].get("range")
        self.damage_ = towerData[self.upgrade_level_ -1].get("damage")
        self.attackCD_ = towerData[self.upgrade_level_ - 1].get("cooldown")
        self.upcost_ = towerData[self.upgrade_level_ - 1].get("upcost")
        self.cdCounter_ = 0
        projectile_image = pygame.image.load("Assets/Sprites/Projectiles/Arrow.png").convert_alpha()

        self.projectile_image_ = pygame.transform.scale(projectile_image,(20,40))
 

    def update(self, enemyGroup,projectileGroup):
        if self.cdCounter_ > 0:
            self.cdCounter_ -= 1
        
        targetEnemy = self.getTargetEnemy(enemyGroup)
        if targetEnemy and self.cdCounter_ == 0:
            self.attack(targetEnemy,projectileGroup)
            self.cdCounter_ = self.attackCD_
    

    def getTargetEnemy(self, enemyGroup):
        targetEnemy = None
        furthest_progress = -1

        for enemy in enemyGroup:
            if self.isWithinRange(enemy):
                progress = enemy.target_waypoint
                if progress > furthest_progress:
                    furthest_progress = progress
                    targetEnemy = enemy

        return targetEnemy
    
    def isWithinRange(self, enemy):
        distance = self.calculateDistance(enemy)
        return distance <= self.range_
    
    
    def calculateDistance(self, enemy):
        enemy_pos = enemy.rect.center
        tower_pos = self.rect.center
        return math.hypot(enemy_pos[0] - tower_pos[0], enemy_pos[1] - tower_pos[1])
    
    
    def attack(self,enemy,projectileGroup):
        direction = pygame.math.Vector2(enemy.rect.center) - pygame.math.Vector2(self.rect.center)
        angle_rad = math.atan2(direction.y, direction.x)
        angle_deg = math.degrees(angle_rad) + 180
        rotated_projectile = pygame.transform.rotate(self.projectile_image_, -angle_deg)

        adjusted_pos = (self.rect.centerx - rotated_projectile.get_width() / 2, self.rect.centery - rotated_projectile.get_height())
        projectile = Projectile(rotated_projectile, adjusted_pos, enemy, self.damage_)
        projectileGroup.add(projectile)

    def drawRange(self,surface):
        surface.blit(self.image, self.rect)
        pygame.draw.circle(surface, constants.LIGHT_GREY, (int(self.X_), int(self.Y_)), self.range_, 1)

    def upgrade(self):
        self.upgrade_level_ += 1
        self.range_ = towerData[self.upgrade_level_ - 1].get("range")
        self.damage_ = towerData[self.upgrade_level_ -1].get("damage")
        self.attackCD_ = towerData[self.upgrade_level_ - 1].get("cooldown")
        self.upcost_ = towerData[self.upgrade_level_ - 1].get("upcost")

    def get_position(self):
            return (int(self.X_), int(self.Y_))
