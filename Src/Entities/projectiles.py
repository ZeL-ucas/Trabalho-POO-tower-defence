import pygame
import math
class Projectile(pygame.sprite.Sprite):
    def __init__(self, image, start_pos, target, damage):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.original_image = image
        self.rect = self.image.get_rect()
        self.rect.center = start_pos
        self.target = target
        self.damage = damage
        self.speed = 7

    def update(self):
        direction = pygame.math.Vector2(self.target.rect.center) - pygame.math.Vector2(self.rect.center)
        distance = direction.length()
        if distance <= self.speed:
            self.target.take_damage(self.damage)
            self.kill()

        else:
            direction = direction.normalize() * self.speed
            self.rect.move_ip(direction)

