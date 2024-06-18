import pygame
import math
from Interfaces.projectilesInterface import InterfaceProjectiles

class Projectile(pygame.sprite.Sprite, InterfaceProjectiles):
    def __init__(self, image, start_pos, target, damage) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = start_pos
        self.target = target
        self.damage = damage
        self.speed = 3

    def update(self) -> None:
        direction = pygame.math.Vector2(self.target.rect.center) - pygame.math.Vector2(self.rect.center)
        distance = direction.length()
        if distance <= self.speed:
            self.target.takeDamage(self.damage)
            self.kill()

        else:
            direction = direction.normalize() * self.speed
            self.rect.move_ip(direction)

