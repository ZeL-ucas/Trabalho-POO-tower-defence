import pygame
from pygame.math import Vector2
import math
from Utils import constants

#pygame sprit class

class Enemy(pygame.sprite.Sprite ):          #A classe Enemy herdará as propriedades da classe Sprite
    def __init__(self, waypoints, image,death_callback=None):
        pygame.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.position = Vector2(self.waypoints[0])
        self.target_waypoint = 1 
        self.speed = constants.classicEnemySpeed
        self.angle = 0
        self.health_ = constants.classicEnemyHealth
        self.original_image = image
        self.image = pygame.transform.rotate(self.original_image, self.angle) 
        self.rect = self.image.get_rect()   #self.rect é derivado da image. E, get_rect() é um método
        self.rect.center = self.position         #posiciona os retângulos center na variável position
        self.flash_time = 0 
        self.death_callback = death_callback
        self.bounty = 50 #valor de ouro pra quando o inimigo morrer 

    def update(self):
        self.move()
        self.rotate()
        if self.flash_time > 0:
            self.flash_time -= 1
            if self.flash_time == 0:
                self.image = pygame.transform.rotate(self.original_image, self.angle)
    def move(self):
        #target waypoint:
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.position 

        else:
            #enemy chegou ao fim do caminho
            self.kill()
        #Distance to target
        distance = self.movement.length()

        #Distance is greater than the enemy speed
        if distance >= self.speed:
            self.position += self.movement.normalize() * self.speed
        else:
            if distance != 0:
                self.position += self.movement.normalize() * distance
            self.target_waypoint += 1

    def rotate(self):
        #distance to next waypoint
        distance = self.target - self.position

        #angle
        self.angle = math.degrees(math.atan2(-distance[1], distance[0]))

        #rotate image, update rectangle
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()   
        self.rect.center = self.position

    def take_damage(self, damage):
        self.health_ -= damage
        self.flash_time = 1  # Configurar o tempo de flash para um frame
        self.image = pygame.transform.rotate(self.original_image.copy(), self.angle)  # Cópia da imagem original
        self.image.fill((255, 0, 0), special_flags=pygame.BLEND_MULT)  # Aplicar efeito de flash vermelho
        if self.health_ <= 0:
            self.kill()

    def kill(self):
        if self.death_callback:
            self.death_callback(self.bounty)  # Passar o valor de ouro para o callback de morte
        super().kill()
  