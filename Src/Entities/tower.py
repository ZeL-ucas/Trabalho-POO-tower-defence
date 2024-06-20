from Utils import constants
import pygame
import math
import random
from Entities.enemy import Enemy
from .projectiles import Projectile
from Utils.towerData import towerClassic
from Interfaces.towerInterface import InterfaceTower
from Utils.functions import loadAnimation, playAnimation

class Tower(pygame.sprite.Sprite, InterfaceTower):
    def __init__(self,image: pygame.Surface, posX: int, posY: int)->None :
        pygame.sprite.Sprite.__init__(self)
        self.posX_ = posX
        self.posY_ = posY
        self.price = constants.priceClassic
        self.X_ = (self.posX_ + 0.5) * constants.tileSize
        self.Y_ = (self.posY_ + 0.2) * constants.tileSize
        self.imageBase = pygame.transform.scale(image, (48, 80))
        self.rect = self.imageBase.get_rect()
        self.rect.center = (self.X_, self.Y_)
        self.rectBase = self.imageBase.get_rect()
        self.rectBase.center = (self.X_, self.Y_)

        self.upgrade_level_ = 1
        self.range_ = towerClassic[self.upgrade_level_ - 1].get("range")
        self.damage_ = towerClassic[self.upgrade_level_ -1].get("damage")
        self.attackCD_ = towerClassic[self.upgrade_level_ - 1].get("cooldown")
        self.upcost_ = towerClassic[self.upgrade_level_ - 1].get("upcost")
        self.cdCounter_ = 0
        self.zap = False
        self.zapper_timer = 0
        self.active = True
    
        self.projectile_image_ = pygame.image.load("Assets/Sprites/Projectiles/TowerBase/base_projectile.png").convert_alpha()
        self.projectile_image_ = pygame.transform.scale(pygame.image.load("Assets/Sprites/Projectiles/TowerBase/base_projectile.png").convert_alpha(), (120, 120))
        self.sprite_sheet = pygame.image.load("Assets/Sprites/Towers/TowerClassic/towerClassicTop.png").convert_alpha()
        self.frames = constants.ANIMATION_STEPS_TOWER
        self.animation_list = loadAnimation(self.sprite_sheet, self.frames)
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image_weapon = self.animation_list[self.frame_index]
        self.image = self.image_weapon
        self.original_image = self.image.copy()

    def update(self, enemyGroup: pygame.sprite.Group, projectileGroup: pygame.sprite.Group, surface: pygame.Surface) -> None:
        self.screen = surface
        if self.active:
            self.image, self.frame_index, self.update_time = playAnimation(
                self.animation_list, self.frame_index, 0, (self.X_, self.Y_ - 20), self.update_time, 75
        )
        if self.frame_index == 20:
            self.frame_index = 0
            
        if self.zap:
            if self.zapper_timer > 0:
                self.zapper_timer -= 1
                self.active = False

            else:
                self.active = True
                self.zap = False
                self.image = self.original_image
        else:
            if self.cdCounter_ > 0:
                self.cdCounter_ -= 1
            
            targetEnemy = self.getTargetEnemy(enemyGroup)
            if targetEnemy and self.cdCounter_ == 0:
                self.attack(targetEnemy, projectileGroup)
                self.cdCounter_ = self.attackCD_

        self.rect = self.image.get_rect()
        self.rect.center = (self.X_, self.Y_ - 20)
    # Desenhe a imagem base primeiro
        surface.blit(self.imageBase, self.rectBase)
    
    # Depois, desenhe a imagem da torre
        surface.blit(self.image, self.rect)

    # Se está paralisada, desenha os raios
        if self.zap:
            self.drawRays(surface, self.rect.centerx, self.rect.centery)

    def getTargetEnemy(self, enemyGroup: pygame.sprite.Group) -> None:
        targetEnemy = None
        furthest_progress = -1

        for enemy in enemyGroup:
            if self.isWithinRange(enemy):
                progress = enemy.target_waypoint
                if progress > furthest_progress:
                    furthest_progress = progress
                    targetEnemy = enemy

        return targetEnemy
    
    def isWithinRange(self, enemy: Enemy)->float:
        distance = self.calculateDistance(enemy)
        return distance <= self.range_
    
    
    def calculateDistance(self, enemy: Enemy)->float:
        enemy_pos = enemy.rect.center
        tower_pos = self.rect.center
        return math.hypot(enemy_pos[0] - tower_pos[0], enemy_pos[1] - tower_pos[1])
    
    
    def attack(self,enemy: Enemy,projectileGroup: pygame.sprite.Group)->None:
        direction = pygame.math.Vector2(enemy.rect.center) - pygame.math.Vector2(self.rect.center)
        angle_rad = math.atan2(direction.y, direction.x)
        angle_deg = math.degrees(angle_rad) + 180
        rotated_projectile = pygame.transform.rotate(self.projectile_image_, -angle_deg)
        
        adjusted_pos = (self.rect.centerx, self.rect.centery)  
        projectile = Projectile(rotated_projectile, adjusted_pos, enemy, self.damage_)
        projectileGroup.add(projectile)

    def drawRange(self,surface: pygame.Surface)->None:
        surface.blit(self.image, self.rect)

        pygame.draw.circle(surface, constants.LIGHT_GREY, (int(self.X_), int(self.Y_)), self.range_, 1)

    def zapper(self, duration: int)->None:
        self.zap = True
        self.zapper_timer = (self.attackCD_  *duration) 

    def getPosition(self)->tuple:
            return (int(self.X_), int(self.Y_))

    def upgrade(self)->None:
        self.upgrade_level_ += 1
        self.range_ = towerClassic[self.upgrade_level_ - 1].get("range")
        self.damage_ = towerClassic[self.upgrade_level_ -1].get("damage")
        self.attackCD_ = towerClassic[self.upgrade_level_ - 1].get("cooldown")
        self.upcost_ = towerClassic[self.upgrade_level_ - 1].get("upcost")

    @staticmethod
    def drawRays(surface: pygame.Surface, x: int, y: int) -> None:
        for _ in range(constants.zapperQuant):
            angle = random.uniform(0, 2 * math.pi)
            length = random.uniform(constants.zapperRadius // 2, constants.zapperRadius)
            x_end = x + length * math.cos(angle)
            y_end = y + length * math.sin(angle)
            cor = constants.YELLOW if random.random() > 0.67 else constants.LIGHT_GREY
            pygame.draw.line(surface, cor, (x, y), (x_end, y_end), 2)
