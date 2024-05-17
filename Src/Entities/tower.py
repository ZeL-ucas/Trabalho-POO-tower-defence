from Utils import constants
import pygame
import math

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

    def update(self, enemyGroup):
        if self.cdCounter_ > 0:
            self.cdCounter_ -= 1
        
        closest_enemy = self.get_closest_enemy(enemyGroup)
        if closest_enemy and self.cdCounter_ == 0:
            self.attack(closest_enemy)
            self.cdCounter_ = self.attackCD_
    

    def get_closest_enemy(self, enemyGroup):
        closest_enemy = None
        closest_distance = self.range_

        for enemy in enemyGroup:
            distance = self.calculate_distance(enemy)
            if distance < closest_distance:
                closest_enemy = enemy
                closest_distance = distance
    

        return closest_enemy
    
    def calculate_distance(self, enemy):
        enemy_pos = enemy.rect.center
        tower_pos = self.rect.center
        return math.hypot(enemy_pos[0] - tower_pos[0], enemy_pos[1] - tower_pos[1])
    
    def attack(self,enemy):
        enemy.take_damage(self.damage_)
        print(self,"atirou")

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        pygame.draw.circle(surface, (0, 255, 0), (int(self.X_), int(self.Y_)), self.range_, 1)


