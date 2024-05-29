from Utils import constants

import pygame
import math
from .projectiles import Projectile

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
        self.range_ = 150
        self.damage_ = 10
        self.attackCD_ = 30
        self.cdCounter_ = 0
        projectile_image = pygame.image.load("Assets/Sprites/Projectiles/Arrow.png").convert_alpha()

        self.projectile_image_ = pygame.transform.scale(projectile_image,(20,40))
        self.frozen = False
        self.freeze_timer = 0
        self.original_image = self.image.copy()

 

    def update(self, enemyGroup,projectileGroup):
        if self.frozen:
            if self.freeze_timer > 0:
                self.freeze_timer -= 1
            else:
                self.frozen = False
                self.image = self.original_image
        else:
            if self.cdCounter_ > 0:
                self.cdCounter_ -= 1
            
            targetEnemy = self.getTargetEnemy(enemyGroup)
            if targetEnemy and self.cdCounter_ == 0:
                self.attack(targetEnemy, projectileGroup)
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

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        #pygame.draw.circle(surface, (0, 255, 0), (int(self.X_), int(self.Y_)), self.range_, 1)
        #removi o range por enquanto

    def freeze(self, duration):
        self.frozen = True
        self.freeze_timer = (self.attackCD_  *duration)
        frozen_image = self.original_image.copy()
        frozen_image.fill((0, 0, 255), special_flags=pygame.BLEND_MULT)
        self.image = frozen_image
    


