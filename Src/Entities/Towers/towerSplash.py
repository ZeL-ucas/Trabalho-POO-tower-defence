# towerSplash.py
import pygame
from Src.Utils import constants
from Src.Entities.tower import Tower
from Utils.towerData import towerSplash
from Utils.functions import loadAnimation, playAnimation

class TowerSplash(Tower):
    def __init__(self, posX: int, posY: int) -> None:
        image = pygame.image.load("Assets/Sprites/Towers/TowerSplash/towerSplashImage.png").convert_alpha()
        super().__init__(image, posX, posY)
        
        # Remover lógica de projétil e sprites separados
        self.frames = constants.ANIMATION_STEPS_TOWER_SPLASH
        self.sprite_sheet = pygame.image.load("Assets/Sprites/Towers/TowerSplash/towerSplash.png").convert_alpha()
        self.animation_list = loadAnimation(self.sprite_sheet, self.frames)
        self.imageTower = self.animation_list[self.frame_index]
        self.image = self.imageTower
        self.range_ = towerSplash[self.upgrade_level_ - 1].get("range")
        self.damage_ = towerSplash[self.upgrade_level_ - 1].get("damage")
        self.attackCD_ = towerSplash[self.upgrade_level_ - 1].get("cooldown")
        self.upcost_ = towerSplash[self.upgrade_level_ - 1].get("upcost")
        self.cdCounter_ = 0  # Cooldown counter

    def update(self, enemyGroup: pygame.sprite.Group, projectileGroup: pygame.sprite.Group, surface: pygame.Surface) -> None:
        if self.active:
            self.image, self.frame_index, self.update_time = playAnimation(
                self.animation_list, self.frame_index, 0, (self.X_, self.Y_ - 20), self.update_time, 75
            )
            if self.frame_index == self.frames:
                self.frame_index = 0
        if self.cdCounter_ > 0: 
            self.cdCounter_ -= 1
        if self.zap:
            if self.zapper_timer > 0:
                self.zapper_timer -= 1
                self.active = False

            else:
                self.active = True
                self.zap = False
                self.image = self.original_image
                
        if self.cdCounter_ == 0:
            self.attack(enemyGroup)
            self.cdCounter_ = self.attackCD_

        self.rect = self.image.get_rect()
        self.rect.center = (self.X_, self.Y_ - 20)
        
        surface.blit(self.image, self.rect)
        
        # Se está paralisada, desenha os raios
        if self.zap:
            self.drawRays(surface, self.rect.centerx, self.rect.centery)

    def attack(self, enemyGroup: pygame.sprite.Group) -> None:
        for enemy in enemyGroup:
            if self.isWithinRange(enemy):
                enemy.takeDamage(self.damage_)

    def isWithinRange(self, enemy) -> bool:
        return self.calculateDistance(enemy) <= self.range_
