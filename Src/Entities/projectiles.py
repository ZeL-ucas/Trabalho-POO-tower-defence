import pygame
from Utils import constants
from Interfaces.projectilesInterface import InterfaceProjectiles
from Entities.enemy import Enemy


class Projectile(pygame.sprite.Sprite, InterfaceProjectiles):
    def __init__(self, image: pygame.Surface, start_pos: tuple, target: Enemy, damage: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = start_pos
        self.target = target
        self.damage = damage
        self.speed = constants.projectileSpeed

    def update(self) -> None:
        direction = pygame.math.Vector2(self.target.rect.center) - pygame.math.Vector2(self.rect.center)
        distance = direction.length()
        if distance <= self.speed:
            self.target.takeDamage(self.damage)
            self.kill()

        else:
            direction = direction.normalize() * self.speed
            self.rect.move_ip(direction)

