import pygame

import time
from Src.Utils import constants
from Src.Entities.enemy import Enemy
from Src.Interfaces.healerInterface import InterfaceHealer
from Utils.functions import loadAnimation
class Healer(Enemy,InterfaceHealer):

    def __init__(self, waypoints: list, enemy_group: pygame.sprite.Group, surface: pygame.Surface ,death_callback=None ) -> None:
        image = pygame.image.load("Assets/Sprites/Enemys/Healer/healer.png").convert_alpha()
        special_sprite_sheet = pygame.image.load("Assets/Sprites/Enemys/Healer/healer_special.png").convert_alpha()
        self.surface = surface
        super().__init__(waypoints, constants.ANIMATION_STEPS_ENEMY_HEALER, image, "healer", death_callback)
        self.enemy_group = enemy_group
        self.heal_radius = constants.healRadius
        self.heal_amount = constants.healAmount
        self.last_heal_time = time.time()
        self.heal_interval = constants.healInterval
        self.bounty = constants.bountyHealer
        self.is_healing = False
        self.healing_start_time = 0
        self.healing_duration = 1  
        self.healing_frame_duration = 1/constants.ANIMATION_STEPS_ENEMY_HEALER_SPECIAL
        self.healing_frames = loadAnimation(special_sprite_sheet, constants.ANIMATION_STEPS_ENEMY_HEALER_SPECIAL)
        self.current_healing_frame = 0

    #realiza o update padrao dos inimigos mas a cada alguns segundos ele cura um pouco 
    def update(self) -> None:
        super().update()
        current_time = time.time()
        if self.is_healing:
            if current_time - self.healing_start_time >= self.healing_duration:
                self.is_healing = False
                # self.image = self.original_image
            else:
                frame_index = int((current_time - self.healing_start_time) / self.healing_frame_duration) % len(self.healing_frames)
                healing_frame = self.healing_frames[frame_index]
                self.image = pygame.transform.rotate(healing_frame, self.angle)
        if current_time - self.last_heal_time >= self.heal_interval:
            self.healNearbyEnemies()
            self.last_heal_time = current_time
    
    #checa os inimigos proximos
    def healNearbyEnemies(self) -> None:
        self.health_ += self.heal_amount
        if self.health_ > self.max_health_:
            self.health_ = self.max_health_
        for enemy in self.enemy_group:
            if enemy != self and self.position.distance_to(enemy.position) <= self.heal_radius:
                self.applyHeal(enemy)


    def applyHeal(self, enemy: Enemy) -> None:
        self.is_healing = True
        self.healing_start_time  = time.time()
        max_health = enemy.getMaxHealth()  
        enemy.health_ += self.heal_amount
        pygame.draw.circle(self.surface, constants.MUSTARD_YELLOW, (int(self.position[0]), int(self.position[1])), self.heal_radius, 1)
        if enemy.health_ > max_health:
            enemy.health_ = max_health
        """
        Aplica a cura a um inimigo específico, desenha o curador na superfície e desenha um círculo 
        representando o raio de cura. Garante que a vida do inimigo não exceda sua vida máxima.
        """