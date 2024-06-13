import pygame

import time
from Src.Utils import constants
from Src.Entities.enemy import Enemy
from Src.Interfaces.healerInterface import InterfaceHealer
class Healer(Enemy,InterfaceHealer):

    def __init__(self, waypoints:list,enemy_group:pygame.sprite.Group, surface:pygame.Surface ,death_callback=None )->None:
        image = pygame.image.load("Assets/Sprites/Enemys/Healer/healer.png").convert_alpha()
        special_sprite_sheet = pygame.image.load("Assets/Sprites/Enemys/Healer/healer_special.png").convert_alpha()
        self.surface = surface
        super().__init__(waypoints, constants.ANIMATION_STEPS_ENEMY_HEALER, image, death_callback)
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
        self.is_healing = False
        self.healing_start_time = 0
        self.healing_duration = 1  
        self.healing_frame_duration = 1/constants.ANIMATION_STEPS_ENEMY_HEALER_SPECIAL
        self.healing_frames = self.load_healing_frames(special_sprite_sheet, constants.ANIMATION_STEPS_ENEMY_HEALER_SPECIAL)
        self.current_healing_frame = 0

    def load_healing_frames(self, sprite_sheet:pygame.Surface, frames:int):
        width = sprite_sheet.get_width() // frames
        height = sprite_sheet.get_height()
        frame_images = []
        for i in range(frames):
            frame = sprite_sheet.subsurface(pygame.Rect(i * width, 0, width, height))
            frame_images.append(frame)
        return frame_images
    
    #realiza o update padrao dos inimigos mas a cada alguns segundos ele cura um pouco 
    def update(self)->None:
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
        self.is_healing = True
        self.healing_start_time  = time.time()
        max_health = enemy.get_max_health()  
        enemy.health_ += self.heal_amount
        pygame.draw.circle(self.surface, constants.MUSTARD_YELLOW, (int(self.position[0]), int(self.position[1])), self.heal_radius, 1)
        if enemy.health_ > max_health:
            enemy.health_ = max_health
        """
        Aplica a cura a um inimigo específico, desenha o curador na superfície e desenha um círculo 
        representando o raio de cura. Garante que a vida do inimigo não exceda sua vida máxima.
        """