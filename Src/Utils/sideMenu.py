import pygame
from Interfaces.sideMenuInterface import sideMenuInterface

class SideMenu(sideMenuInterface):
    def __init__(self, x:int, y:int, image:pygame.Surface, singleClick:bool):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.singleClick = singleClick
    
    def draw(self, surface:pygame.Surface) -> bool:
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                if self.singleClick:
                    self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        surface.blit(self.image, self.rect)
        return action