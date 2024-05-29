import pygame
from Src.Utils import functions
from Src.Utils import constants
from Src.Entities.enemy import Enemy
import math

class Frezzer(Enemy):
    def __init__(self, waypoints,towerGroup_, death_callback=None) -> None:
        image = "Assets/Sprites/Enemys/Voidbutterfly.png"
        sprites = functions.load_sprite_sheet(image,9,10)
        self.static = sprites[0][0]
        super().__init__(waypoints, self.static, death_callback)
        self.health_= constants.frezzerHealth
        self.speed = constants.frezzerSpeed
        self.lifes =constants.frezzerLifes
        self.bounty = 30
        self.towerGroup = towerGroup_

    def kill(self, killed: bool) -> None:
        if self.alive:
            self.alive = False

            if killed:
                self.freeze_nearest_tower()
            if self.death_callback:
                self.death_callback(self.bounty, killed, self.lifes)
            pygame.sprite.Sprite.kill(self)

    def freeze_nearest_tower(self):
        nearest_tower = None
        shortest_distance = float('inf')
        
        for tower in self.towerGroup:
            distance = math.hypot(self.rect.centerx - tower.rect.centerx, self.rect.centery - tower.rect.centery)
            if distance < shortest_distance:
                shortest_distance = distance
                nearest_tower = tower

        if nearest_tower:
            nearest_tower.freeze(constants.freezeDuration)