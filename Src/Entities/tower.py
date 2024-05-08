import pygame


class Tower(pygame.sprite.Sprite):
    def __init__(self,image,posX, posY) -> None : # colocar no construtor depois mousePosX,mousePosY
        pygame.sprite.Sprite.__init__(self)
        self.posX_ = posX
        self.posY_ = posY
        self.price = 500
        #self.X_ = (self.PosX_ + 0.5) * constats.tileSize
        #self.Y_ = (self.PosY_ + 0.5) * constats.tileSize
        self.image_ = image
        self.rect_ = self.image_.get_rect()
        self.rect_.center = (posX,posY)