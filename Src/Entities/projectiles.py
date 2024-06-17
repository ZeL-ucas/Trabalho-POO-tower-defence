import pygame
import math
from Interfaces.projectilesInterface import InterfaceProjectiles
from Utils.functions import playAnimation, loadAnimation

class Projectile(pygame.sprite.Sprite, InterfaceProjectiles):
    def __init__(self, image, start_pos, target, damage) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(center=start_pos)
        self.target = target
        self.damage = damage
        self.speed = 4
        self.update_time = pygame.time.get_ticks()
        self.frames = 12
        self.animation_list = loadAnimation(self.image, self.frames)
        self.frame_index = 0
        self.angle = 0

    def update(self) -> None:
        direction = pygame.math.Vector2(self.target.rect.center) - pygame.math.Vector2(self.rect.center)
        distance = direction.length()

        if distance <= self.speed:
            self.target.takeDamage(self.damage)
            self.kill()
        else:
            direction = direction.normalize() * self.speed
            self.rect.move_ip(direction)
            self.angle = math.degrees(math.atan2(-direction.y, direction.x))

        self.image, self.frame_index, self.update_time = playAnimation(
            self.animation_list, self.frame_index, self.angle, self.rect.center, self.update_time, 100
        )

        self.rect = self.image.get_rect(center=self.rect.center)
