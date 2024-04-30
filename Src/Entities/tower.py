import pygame 

class Tower(pygame.sprite.Sprite):
    def __init__(self, image_, pos_):
        pygame.sprite.Sprite.__init__(self)
        self.image_ = image_
        self.rect = self.image_.get_rect()
        self.rect.center = pos_
    def update(self):
        pass 