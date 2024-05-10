import pygame
from pygame.math import Vector2
import math

#pygame sprit class

class Enemy(pygame.sprite.Sprite):          #A classe Enemy herdará as propriedades da classe Sprite
    def __init__(self, waypoints, image):
        pygame.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.position = Vector2(self.waypoints[0])
        self.target_waypoint = 1 
        self.speed = 1
        self.angle = 0
        self.original_image = image
        self.image = pygame.transform.rotate(self.original_image, self.angle) 
        self.rect = self.image.get_rect()   #self.rect é derivado da image. E, get_rect() é um método
        self.rect.center = self.position         #posiciona os retângulos center na variável position

    def update(self):
        self.move()
        self.rotate()
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

