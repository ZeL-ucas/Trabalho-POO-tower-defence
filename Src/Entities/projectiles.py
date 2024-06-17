import pygame
import math
from Interfaces.projectilesInterface import InterfaceProjectiles
from Utils.functions import loadAnimation, playAnimation

class Projectile(pygame.sprite.Sprite, InterfaceProjectiles):
    def __init__(self, image, start_pos, target, damage) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.original_image = image
        self.frame_index = 0
        self.rect = self.image.get_rect()
        self.rect.center = start_pos
        self.target = target
        self.damage = damage
        self.speed = 7
        self.animation_list = loadAnimation(self.image, 12)
        self.update_time = pygame.time.get_ticks()


    def update(self) -> None:
        direction = pygame.math.Vector2(self.target.rect.center) - pygame.math.Vector2(self.rect.center)
        distance = direction.length()
        self.image, self.frame_index, self.update_time = playAnimation(
            self.animation_list, self.frame_index, 0, (direction), self.update_time, 10
        )
        if distance <= self.speed:
            self.target.takeDamage(self.damage)
            self.kill()

        else:
            direction = direction.normalize() * self.speed
            self.rect.move_ip(direction)

