import pygame
from Src.Entities.enemy import Enemy
from Interfaces.zapperInterface import InterfaceZapper
from Src.Utils import constants
import math

class Zapper(Enemy, InterfaceZapper):
    def __init__(self, waypoints:list,towerGroup_:pygame.sprite.Group, death_callback=None) -> None:
        image = pygame.image.load("Assets/Sprites/Enemys/Zapper/zapper.png").convert_alpha()
        super().__init__(waypoints, constants.ANIMATION_STEPS_ENEMY_ZAPPER, image, "zapper", death_callback)
        self.bounty = constants.bountyZapper
        self.towerGroup = towerGroup_

    def kill(self, killed: bool) -> None:
        if self.alive:
            self.alive = False

            if killed:
                self.zapperNearestTower()
            if self.death_callback:
                self.death_callback(self.bounty, killed, self.lifes)
            pygame.sprite.Sprite.kill(self)

    def zapperNearestTower(self) -> None:
        nearest_tower = None
        shortest_distance = float('inf')
        
        for tower in self.towerGroup:
            distance = math.hypot(self.rect.centerx - tower.rect.centerx, self.rect.centery - tower.rect.centery)
            if distance < shortest_distance:
                shortest_distance = distance
                nearest_tower = tower

        if nearest_tower:
            nearest_tower.zapper(self.zapperDuration)
    """
    Este código define a lógica de um inimigo do tipo Zapper que, ao morrer, congela 
    a torre mais próxima. A funcionalidade de congelamento específica precisaria ser 
    implementada na classe da torre com um método zapper.
    """