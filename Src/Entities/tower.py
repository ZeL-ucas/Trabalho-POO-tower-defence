from Utils import constants
import pygame


class Tower(pygame.sprite.Sprite):
    def __init__(self,image,posX, posY) -> None : # colocar no construtor depois mousePosX,mousePosY
        pygame.sprite.Sprite.__init__(self)
        self.posX_ = posX
        self.posY_ = posY
        self.price = 500
        self.X_ = (self.posX_ + 0.5) * constants.tileSize
        self.Y_ = (self.posY_ + 0.2) * constants.tileSize #valor diferente para a torre atual não ficar em cima dos blocos
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.X_, self.Y_)

