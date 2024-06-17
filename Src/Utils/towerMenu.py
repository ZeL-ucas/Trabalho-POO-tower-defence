import pygame
import math
from Utils import constants

class TowerMenu:
    def __init__(self, tower, screen, upgrade_image):
        self.screen_ = screen
        self.tower = tower
        self.upgrade_image = upgrade_image
        self.upgrade_rect = upgrade_image.get_rect()
        self.radius = 50

    def draw(self):
        tower_pos = self.tower.getPosition()
        pygame.draw.circle(self.screen_, constants.SILVER, tower_pos, self.radius, 1)
        self.tower.drawRange(self.screen_)
        angle = math.radians(30) 
        button_x = tower_pos[0] + self.radius * math.cos(angle) - self.upgrade_rect.width // 2
        button_y = tower_pos[1] - self.radius * math.sin(angle) - self.upgrade_rect.height // 2
        
        self.screen_.blit(self.upgrade_image, (button_x, button_y))

    def is_clicked(self, mouse_pos):
        button_x = self.tower.getPosition()[0] + self.radius * math.cos(math.radians(45)) - self.upgrade_rect.width // 2
        button_y = self.tower.getPosition()[1] - self.radius * math.sin(math.radians(45)) - self.upgrade_rect.height // 2
        button_rect = pygame.Rect(button_x, button_y, self.upgrade_rect.width, self.upgrade_rect.height)
        return button_rect.collidepoint(mouse_pos)
