from Utils import constants
import pygame
import math
import random
from .projectiles import Projectile
from Utils.towerData import towerData
from Interfaces.towerInterface import InterfaceTower

class Tower(pygame.sprite.Sprite, InterfaceTower):
    def __init__(self,image:pygame.Surface,posX:int, posY:int)->None : # colocar no construtor depois mousePosX,mousePosY
        pygame.sprite.Sprite.__init__(self)
        self.posX_ = posX
        self.posY_ = posY
        self.price = 50
        self.X_ = (self.posX_ + 0.5) * constants.tileSize
        self.Y_ = (self.posY_ + 0.2) * constants.tileSize #valor diferente para a torre atual não ficar em cima dos blocos
        self.imageBase = image
        self.rect = self.imageBase.get_rect()
        self.rect.center = (self.X_, self.Y_)
        self.rectBase = self.imageBase.get_rect()
        self.rectBase.center = (self.X_, self.Y_)

        self.upgrade_level_ = 1
        self.range_ = towerData[self.upgrade_level_ - 1].get("range")
        self.damage_ = towerData[self.upgrade_level_ -1].get("damage")
        self.attackCD_ = towerData[self.upgrade_level_ - 1].get("cooldown")
        self.upcost_ = towerData[self.upgrade_level_ - 1].get("upcost")
        self.cdCounter_ = 0
        projectile_image = pygame.image.load("Assets/Sprites/Projectiles/Arrow.png").convert_alpha()
        self.projectile_image_ = pygame.transform.scale(projectile_image,(20,40))
        self.zap = False
        self.zapper_timer = 0


 
        self.sprite_sheet = pygame.image.load("Assets/Sprites/Towers/TowerClassicTop.png")
        self.animation_list = self.load_images()
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image_weapon = self.animation_list[self.frame_index]
        self.image = self.image_weapon
        self.original_image = self.image.copy()

    def update(self, enemyGroup:pygame.sprite.Group,projectileGroup:pygame.sprite.Group,surface:pygame.Surface) -> None:
        self.screen = surface
        if self.zap:
            if self.zapper_timer > 0:
                self.zapper_timer -= 1
            else:
                self.zap = False
                self.image = self.original_image
        else:
            if self.cdCounter_ > 0:
                self.cdCounter_ -= 1
            
            targetEnemy = self.getTargetEnemy(enemyGroup)
            if targetEnemy and self.cdCounter_ == 0:
                self.attack(targetEnemy, projectileGroup)
                self.cdCounter_ = self.attackCD_
        self.play_animation()
    
    # Desenhe a imagem base primeiro
        surface.blit(self.imageBase, self.rectBase)
    
    # Depois, desenhe a imagem da torre
        surface.blit(self.image, self.rect)
    # Se está paralisada, desenha os raios
        if self.zap:
            self.draw_rays(surface, self.rect.centerx, self.rect.centery)

    def getTargetEnemy(self, enemyGroup:pygame.sprite.Group) -> None:
        targetEnemy = None
        furthest_progress = -1

        for enemy in enemyGroup:
            if self.isWithinRange(enemy):
                progress = enemy.target_waypoint
                if progress > furthest_progress:
                    furthest_progress = progress
                    targetEnemy = enemy

        return targetEnemy
    
    def isWithinRange(self, enemy)->float:
        distance = self.calculateDistance(enemy)
        return distance <= self.range_
    
    
    def calculateDistance(self, enemy)->float:
        enemy_pos = enemy.rect.center
        tower_pos = self.rect.center
        return math.hypot(enemy_pos[0] - tower_pos[0], enemy_pos[1] - tower_pos[1])
    
    
    def attack(self,enemy,projectileGroup:pygame.sprite.Group)->None:
        direction = pygame.math.Vector2(enemy.rect.center) - pygame.math.Vector2(self.rect.center)
        angle_rad = math.atan2(direction.y, direction.x)
        angle_deg = math.degrees(angle_rad) + 180
        rotated_projectile = pygame.transform.rotate(self.projectile_image_, -angle_deg)

        adjusted_pos = (self.rect.centerx - rotated_projectile.get_width() / 2, self.rect.centery - rotated_projectile.get_height())
        projectile = Projectile(rotated_projectile, adjusted_pos, enemy, self.damage_)
        projectileGroup.add(projectile)

    def drawRange(self,surface:pygame.Surface)->None:
        surface.blit(self.image, self.rect)

        pygame.draw.circle(surface, constants.LIGHT_GREY, (int(self.X_), int(self.Y_)), self.range_, 1)

    def zapper(self, duration: int)->None:
        self.zap = True
        self.zapper_timer = (self.attackCD_  *duration) 

    def get_position(self)->tuple:
            return (int(self.X_), int(self.Y_))

    def upgrade(self)->None:
        self.upgrade_level_ += 1
        self.range_ = towerData[self.upgrade_level_ - 1].get("range")
        self.damage_ = towerData[self.upgrade_level_ -1].get("damage")
        self.attackCD_ = towerData[self.upgrade_level_ - 1].get("cooldown")
        self.upcost_ = towerData[self.upgrade_level_ - 1].get("upcost")

    def get_position(self) -> None:
            return (int(self.X_), int(self.Y_))
    
    def load_images(self) -> None:
        # Extract images from spritesheet
        size = self.sprite_sheet.get_height()
        animation_list = []
        for x in range(29):
            temp_img = self.sprite_sheet.subsurface(x * size, 0, size, size)
            animation_list.append(temp_img)
        return animation_list

    def play_animation(self) -> None:
        # Atualizar imagem
        current_time = pygame.time.get_ticks()
        if current_time - self.update_time > 10:  # Atualizar a cada 100ms
            self.frame_index = (self.frame_index + 1) % len(self.animation_list)
            self.update_time = current_time
        self.image = pygame.transform.rotate(self.animation_list[self.frame_index], 0)
        self.rect = self.image.get_rect()
        self.rect.center = (self.X_,(self.Y_ -20 ))

    @staticmethod
    def draw_rays(surface:pygame.Surface, x:int, y:int) -> None:
        for _ in range(constants.zapperQuant):
            angle = random.uniform(0, 2 * math.pi)
            length = random.uniform(constants.zapperRadius // 2, constants.zapperRadius)
            x_end = x + length * math.cos(angle)
            y_end = y + length * math.sin(angle)
            cor = constants.YELLOW if random.random() > 0.67 else constants.LIGHT_GREY
            pygame.draw.line(surface, cor, (x, y), (x_end, y_end), 2)
