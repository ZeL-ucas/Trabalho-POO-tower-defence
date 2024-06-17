import pygame
from pygame.math import Vector2
import math
from Utils import constants
from Interfaces.enemyInterface import InterfaceEnemy
from Utils.functions import loadAnimation, playAnimation
#pygame sprit class

class Enemy(pygame.sprite.Sprite,InterfaceEnemy ):          #A classe Enemy herdará as propriedades da classe Sprite
    def __init__(self, waypoints:list,frames:int, image:pygame.surface, enemy_type: str, death_callback=None)->None:
        pygame.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.position = Vector2(self.waypoints[0])
        self.target_waypoint = 1 

        #atribuição de atributos para cada inimigo diferente, necessário para linkar com as dificuldades
        if enemy_type == "classic":
            self.speed = constants.classicEnemySpeed
            self.health_ = constants.classicEnemyHealth
            self.lifes = constants.classicEnemyLifes
        elif enemy_type == "healer":
            self.speed = constants.healerSpeed
            self.health_ = constants.healerHealth
            self.lifes = constants.healerLifes
        elif enemy_type == "tank":
            self.speed = constants.tankSpeed
            self.health_ = constants.tankHealth
            self.lifes = constants.tankLifes
        elif enemy_type == "zapper":
            self.speed = constants.zapperSpeed
            self.health_ = constants.zapperHealth
            self.lifes = constants.zapperLifes
            self.zapperDuration = constants.zapperDuration

        self.angle = 0
        self.max_health_ = self.health_
        self.original_image = image
        self.rect = self.original_image.get_rect() #self.rect é derivado da image. E, get_rect() é um método
        self.rect.center = self.position #posiciona os retângulos center na variável position
        self.flash_time = 0
        self.death_callback = death_callback
        self.bounty = 50 #valor de ouro pra quando o inimigo morrer 
        self.alive = True
        self.bounty = 50  # valor de ouro pra quando o inimigo morrer

        self.sprite_sheet = self.original_image
        self.frames=frames
        self.animation_list = loadAnimation(self.sprite_sheet, self.frames)       
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image_enemy = self.animation_list[self.frame_index]
        self.image = self.image_enemy
    def update(self):
        self.move()
        self.rotate()
        if self.flash_time > 0:
            self.flash_time -= 1
            if self.flash_time == 0:
                self.image = pygame.transform.rotate(self.animation_list[self.frame_index], self.angle)
        self.image, self.frame_index, self.update_time = playAnimation(self.animation_list, self.frame_index, self.angle, self.position, self.update_time, 100)

    def move(self):
        # Target waypoint
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.position 
        else:
            #enemy chegou ao fim do caminho
            self.kill(False)
        #Distance to target
        distance = self.movement.length()

        # Distance is greater than the enemy speed
        if distance >= self.speed:
            self.position += self.movement.normalize() * self.speed
        else:
            if distance != 0:
                self.position += self.movement.normalize() * distance
            self.target_waypoint += 1

    def rotate(self)->None:
        #distance to next waypoint
        distance = self.target - self.position

        # Angle
        self.angle = math.degrees(math.atan2(-distance[1], distance[0])) + 90

        # Rotate image, update rectangle
        self.image = pygame.transform.rotate(self.animation_list[self.frame_index], self.angle)
        self.rect = self.image.get_rect()   
        self.rect.center = self.position

    def takeDamage(self, damage:int)->None:
        self.health_ -= damage
        self.flash_time = 1  # Configurar o tempo de flash para um frame
        flashed_image = self.animation_list[self.frame_index].copy()
        flashed_image.fill((255, 0, 0), special_flags=pygame.BLEND_MULT)  # Aplicar efeito de flash vermelho
        self.image = pygame.transform.rotate(flashed_image, self.angle)
        if self.health_ <= 0:
            self.kill(True)

    def kill(self,killed:bool)->None:
        if self.alive:
            self.alive = False
            if self.death_callback:
                self.death_callback(self.bounty, killed, self.lifes)
            super().kill()

    def getMaxHealth(self)->int:
        return self.max_health_
        