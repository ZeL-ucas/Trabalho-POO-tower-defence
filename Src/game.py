import pygame
import sys
sys.path.extend(["Src/Utils", "Src/Levels","Src/Entities"])
import constants



pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode(constants.window)

#loop principal
run = True
while (run):

    clock.tick(constants.fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



pygame.quit()