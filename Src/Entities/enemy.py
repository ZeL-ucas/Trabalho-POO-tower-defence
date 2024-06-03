import pygame
from pygame.math import Vector2
import math
from Utils import constants

class Enemy(pygame.sprite.Sprite):
    def __init__(self, waypoints, image, death_callback=None):
        pygame.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.position = Vector2(self.waypoints[0])
        self.target_waypoint = 1 
        self.speed = constants.classicEnemySpeed
        self.angle = 0
        self.health_ = constants.classicEnemyHealth
        self.original_image = image
        self.rect = self.original_image.get_rect() #self.rect é derivado da image. E, get_rect() é um método
        self.rect.center = self.position #posiciona os retângulos center na variável position
        self.flash_time = 0
        self.death_callback = death_callback
        self.bounty = 50  # valor de ouro pra quando o inimigo morrer

        self.sprite_sheet = self.original_image
        self.animation_list = self.load_images()
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
        self.play_animation()

    def move(self):
        # Target waypoint
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.position 
        else:
            # Enemy chegou ao fim do caminho
            self.kill()

        # Distance to target
        distance = self.movement.length()

        # Distance is greater than the enemy speed
        if distance >= self.speed:
            self.position += self.movement.normalize() * self.speed
        else:
            if distance != 0:
                self.position += self.movement.normalize() * distance
            self.target_waypoint += 1

    def rotate(self):
        # Distance to next waypoint
        distance = self.target - self.position

        # Angle
        self.angle = math.degrees(math.atan2(-distance[1], distance[0])) + 90

        # Rotate image, update rectangle
        self.image = pygame.transform.rotate(self.animation_list[self.frame_index], self.angle)
        self.rect = self.image.get_rect()   
        self.rect.center = self.position

    def take_damage(self, damage):
        self.health_ -= damage
        self.flash_time = 1  # Configurar o tempo de flash para um frame
        flashed_image = self.animation_list[self.frame_index].copy()
        flashed_image.fill((255, 0, 0), special_flags=pygame.BLEND_MULT)  # Aplicar efeito de flash vermelho
        self.image = pygame.transform.rotate(flashed_image, self.angle)
        if self.health_ <= 0:
            self.kill()

    def kill(self):
        if self.death_callback:
            self.death_callback(self.bounty)  # Passar o valor de ouro para o callback de morte
        super().kill()

    def load_images(self):
        # Extract images from spritesheet
        size = self.sprite_sheet.get_height()
        animation_list = []
        for x in range(constants.ANIMATION_STEPS_ENEMY):
            temp_img = self.sprite_sheet.subsurface(x * size, 0, size, size)
            animation_list.append(temp_img)
        return animation_list

    def play_animation(self):
        # Atualizar imagem
        current_time = pygame.time.get_ticks()
        if current_time - self.update_time > 100:  # Atualizar a cada 100ms
            self.frame_index = (self.frame_index + 1) % len(self.animation_list)
            self.update_time = current_time
        self.image = pygame.transform.rotate(self.animation_list[self.frame_index], self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
