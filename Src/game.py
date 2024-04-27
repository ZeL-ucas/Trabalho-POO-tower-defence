import pygame
from Utils import constants


pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode(constants.window)
pygame.display.set_caption("defesa blaster ")

#loop principal
run = True
while (run):
    clock.tick(constants.fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



pygame.quit()