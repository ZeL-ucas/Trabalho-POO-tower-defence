import pygame
import math
from Interfaces.projectilesInterface import InterfaceProjectiles
from Utils.functions import play_animation, load_animation

class Projectile(pygame.sprite.Sprite, InterfaceProjectiles):
    def __init__(self, image, start_pos, target, damage) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.original_image = image
        self.rect = self.image.get_rect()
        self.rect.center = start_pos
        self.target = target
        self.damage = damage
        self.speed = 1
        self.angle = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_list = load_animation(self.image, 12)  # Assumindo 12 frames
        self.frame_index = 0

    def update(self) -> None:
        direction = pygame.math.Vector2(self.target.rect.center) - pygame.math.Vector2(self.rect.center)
        distance = direction.length()
        if distance <= self.speed:
            self.target.take_damage(self.damage)
            self.kill()
        else:
            direction = direction.normalize() * self.speed
            self.rect.move_ip(direction)
        self.image, self.frame_index, self.update_time = play_animation(self.animation_list, self.frame_index, self.angle, self.rect.center, self.update_time, 100)
