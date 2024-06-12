import pygame

import time
from Src.Utils import functions
from Src.Utils import constants
from Src.Entities.enemy import Enemy
from Src.Interfaces.healerInterface import InterfaceHealer
class Healer(Enemy,InterfaceHealer):

    def __init__(self, waypoints,enemy_group, surface ,death_callback=None )->None:

        image = pygame.image.load("Assets/Sprites/Enemys/Healer/healer.png").convert_alpha()
        self.surface = surface
        super().__init__(waypoints, 9, image, death_callback)
        self.health_ = constants.healerHealth
        self.max_health_=constants.healerHealth
        self.speed = constants.healerSpeed
        self.enemy_group = enemy_group
        self.heal_radius = 100
        self.heal_amount = 20
        self.last_heal_time = time.time()
        self.heal_interval = 5
        self.lifes = constants.healerLifes
        self.bounty = 80
    #realiza o update padrao dos inimigos mas a cada alguns segundos ele cura um pouco 
    def update(self)->None:
        super().update()
        current_time = time.time()
        if current_time - self.last_heal_time >= self.heal_interval:
            self.heal_nearby_enemies()
            self.last_heal_time = current_time
    
    #checa os inimigos proximos
    def heal_nearby_enemies(self)->None:
        self.health_ += self.heal_amount
        if self.health_ > self.max_health_:
            self.health_ = self.max_health_
        for enemy in self.enemy_group:
            if enemy != self and self.position.distance_to(enemy.position) <= self.heal_radius:
                self.apply_heal(enemy)


    def apply_heal(self, enemy:Enemy)->None:
        max_health = enemy.get_max_health()  
        enemy.health_ += self.heal_amount
        self.surface.blit(self.image, self.rect)
        pygame.draw.circle(self.surface, (0, 255, 0), (int(self.position[0]), int(self.position[1])), self.heal_radius, 1)
        if enemy.health_ > max_health:
            enemy.health_ = max_health

        """
        Aplica a cura a um inimigo específico, desenha o curador na superfície e desenha um círculo 
        representando o raio de cura. Garante que a vida do inimigo não exceda sua vida máxima.
        """