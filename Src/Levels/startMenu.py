import sys
import pygame
from Utils import constants
from Interfaces.startMenuInterface import startMenuInterface

class StartMenu(startMenuInterface):
    def __init__(self):
        pygame.init()
        self.font_ = pygame.font.Font(None, 74)
        self.button_font_ = pygame.font.Font(None, 50)
        self.clock_ = pygame.time.Clock()
        self.screen_ = pygame.display.set_mode(constants.window)
        pygame.display.set_caption('Defesa Blaster')
        self.screen_width_, self.screen_height_ = constants.window
        
        self.easy_button_rect_ = pygame.Rect(self.screen_width_ // 2 - 100, self.screen_height_ // 2 - 50, 200, 50)
        self.medium_button_rect_ = pygame.Rect(self.screen_width_ // 2 - 100, self.screen_height_ // 2 + 50, 200, 50)
        self.hard_button_rect_ = pygame.Rect(self.screen_width_ // 2 - 100, self.screen_height_ // 2 + 150, 200, 50)

    def drawText(self, text: str, font: pygame.font.Font, color: tuple, surface: pygame.Surface, x: int, y: int) -> None:
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect()
        textrect.center = (x, y)
        surface.blit(textobj, textrect)

    def drawButton(self, text: str, font: pygame.font.Font, color: tuple, rect: pygame.Rect, hover:bool) -> None:
        button_color = constants.BROWN_CHOC if hover else constants.BROWN_COFFEE
        pygame.draw.rect(self.screen_, button_color, rect)
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect(center=rect.center)
        self.screen_.blit(textobj, textrect)

    def draw(self) -> None:
        self.screen_.fill(constants.GREEN)
        self.drawText('Defesa Blaster', self.font_, constants.BLACK, self.screen_, self.screen_width_ // 2, self.screen_height_ // 4)
        
        mouse_pos = pygame.mouse.get_pos()
        easy_hover = self.easy_button_rect_.collidepoint(mouse_pos)
        medium_hover = self.medium_button_rect_.collidepoint(mouse_pos)
        hard_hover = self.hard_button_rect_.collidepoint(mouse_pos)
        
        self.drawButton('Fácil', self.button_font_, constants.BLACK, self.easy_button_rect_, easy_hover)
        self.drawButton('Médio', self.button_font_, constants.BLACK, self.medium_button_rect_, medium_hover)
        self.drawButton('Difícil', self.button_font_, constants.BLACK, self.hard_button_rect_, hard_hover)

        pygame.display.update()

    def run(self) -> None:
        run = True
        difficulty = None
        while run:
            self.clock_.tick(constants.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.easy_button_rect_.collidepoint(event.pos):
                        difficulty = 'easy'
                        run = False
                    elif self.medium_button_rect_.collidepoint(event.pos):
                        difficulty = 'medium'
                        run = False
                    elif self.hard_button_rect_.collidepoint(event.pos):
                        difficulty = 'hard'
                        run = False

            self.draw()
        
        return difficulty