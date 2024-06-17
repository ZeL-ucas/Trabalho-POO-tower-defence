import sys
import pygame
from Utils import constants


class EndMenu():
    def __init__(self, outcome: str, score:str):
        pygame.init()
        self.font_ = pygame.font.Font(None, 74)
        self.button_font_ = pygame.font.Font(None, 40)
        self.clock_ = pygame.time.Clock()
        self.screen_ = pygame.display.set_mode(constants.window)
        pygame.display.set_caption('Defesa Blaster')
        self.screen_width_, self.screen_height_ = constants.window
        
        self.quit_button_rect_ = pygame.Rect(self.screen_width_ // 2 - 100, self.screen_height_ // 2, 200, 50)
        self.retry_button_rect_ = pygame.Rect(self.screen_width_ // 2 - 100, self.screen_height_ // 2 + 100, 200, 50)
        self.score = score
        self.outcome = outcome

    def drawText(self, text: str, font: pygame.font.Font, color: tuple, surface: pygame.Surface, x: int, y: int) -> None:
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect()
        textrect.center = (x, y)
        surface.blit(textobj, textrect)

    def drawButton(self, text: str, font: pygame.font.Font, color: tuple, rect: pygame.Rect, hover: bool) -> None:
        button_color = constants.BROWN_CHOC if hover else constants.BROWN_COFFEE
        pygame.draw.rect(self.screen_, button_color, rect)
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect(center=rect.center)
        self.screen_.blit(textobj, textrect)

    def draw(self) -> None:
        self.screen_.fill(constants.GREEN)
        title_text = 'Game Over' if self.outcome == 'lose' else 'Vitória'
        self.drawText(title_text, self.font_, constants.BLACK, self.screen_, self.screen_width_ // 2, self.screen_height_ // 4)
        self.drawText(self.score, self.font_, constants.BLACK, self.screen_, self.screen_width_ // 2, (self.screen_height_ // 4)+40)
        mouse_pos = pygame.mouse.get_pos()
        quit_hover = self.quit_button_rect_.collidepoint(mouse_pos)
        retry_hover = self.retry_button_rect_.collidepoint(mouse_pos)
        
        self.drawButton('Desistir', self.button_font_, constants.BLACK, self.quit_button_rect_, quit_hover)
        self.drawButton('Tentar Novamente', self.button_font_, constants.BLACK, self.retry_button_rect_, retry_hover)

        pygame.display.update()

    def run(self) -> str:
        run = True
        result = None
        while run:
            self.clock_.tick(constants.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.quit_button_rect_.collidepoint(event.pos):
                        result = 'quit'
                        run = False
                    elif self.retry_button_rect_.collidepoint(event.pos):
                        result = 'retry'
                        run = False

            self.draw()
        
        return result