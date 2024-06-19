import pygame
import math
from Utils import constants
from Interfaces.towerMenu import InterfaceTowerMenu
class TowerMenu(InterfaceTowerMenu):
    def __init__(self, tower, screen):
        self.screen_ = screen
        self.tower = tower
        self.upgrade_image =  pygame.image.load("Assets/Sprites/TowerMenu/upgrade_icon.svg").convert_alpha()
        self.upgrade_rect = self.upgrade_image.get_rect()
        self.sell_image = pygame.image.load("Assets/Sprites/TowerMenu/sell_icon.png").convert_alpha()

        self.sell_rect =  self.sell_image.get_rect()
        self.radius = 50

    def draw(self) -> None:
        tower_pos = self.tower.getPosition()
        pygame.draw.circle(self.screen_, constants.SILVER, tower_pos, self.radius, 1)
        self.tower.drawRange(self.screen_)
        angle = math.radians(90) 
        button_x = tower_pos[0] + self.radius * math.cos(angle) - self.upgrade_rect.width // 2
        button_y = tower_pos[1] - self.radius * math.sin(angle) - self.upgrade_rect.height // 2
        
        angle_sell = math.radians(270)
        button_x_sell = tower_pos[0] + self.radius * math.cos(angle_sell) - self.sell_rect.width // 2
        button_y_sell = tower_pos[1] - self.radius * math.sin(angle_sell) - self.sell_rect.height // 2
        self.screen_.blit(self.sell_image, (button_x_sell, button_y_sell))

        self.screen_.blit(self.upgrade_image, (button_x, button_y))

    def is_clicked(self, mouse_pos:tuple)->str:
        tower_pos = self.tower.getPosition()

        button_x_upgrade = tower_pos[0] + self.radius * math.cos(math.radians(90)) - self.upgrade_rect.width // 2
        button_y_upgrade = tower_pos[1] - self.radius * math.sin(math.radians(90)) - self.upgrade_rect.height // 2
        button_rect_upgrade = pygame.Rect(button_x_upgrade, button_y_upgrade, self.upgrade_rect.width, self.upgrade_rect.height)

        button_x_sell = tower_pos[0] + self.radius * math.cos(math.radians(270)) - self.sell_rect.width // 2
        button_y_sell = tower_pos[1] - self.radius * math.sin(math.radians(270)) - self.sell_rect.height // 2
        button_rect_sell = pygame.Rect(button_x_sell, button_y_sell, self.sell_rect.width, self.sell_rect.height)

        if button_rect_upgrade.collidepoint(mouse_pos):
            return 'upgrade'
        elif button_rect_sell.collidepoint(mouse_pos):
            return 'sell'
        return None
