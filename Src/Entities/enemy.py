import pygame

#pygame sprit class

class Enemy(pygame.sprite.Sprite):          #A classe Enemy herdará as propriedades da classe Sprite
    def __init__(self, position, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()   #self.rect é derivado da image. E, get_rect() é um método
        self.rect.center = position         #posiciona os retângulos center na variável position

    def update(self):
        self.move()
    def move(self):
        self.rect.x += 1   #a cada iteração deste jogo, o inimigo moverá 1 pixel para a direita
    




