import pygame
from Utils import constants

class Game():
    def __init__(self):
        pygame.init()
==
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(constants.window)
        pygame.display.set_caption("defesa blaster ")


    def Run(self):
        run = True
        while (run):
            self.clock.tick(constants.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.Quit()

    def Quit(self):
        pygame.quit()