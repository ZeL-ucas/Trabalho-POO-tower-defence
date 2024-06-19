import sys
import pygame
from Utils import constants
from Interfaces.startMenuInterface import startMenuInterface

class StartMenu(startMenuInterface):
    def __init__(self, scores: list):
        pygame.init()
        self.font_ = pygame.font.Font(None, 74)
        self.button_font_ = pygame.font.Font(None, 50)
        self.input_font_ = pygame.font.Font(None, 50)
        self.clock_ = pygame.time.Clock()
        self.screen_ = pygame.display.set_mode(constants.window)
        pygame.display.set_caption('Defesa Blaster')
        self.screen_width_, self.screen_height_ = constants.window
        self.easy_button_rect_ = pygame.Rect(self.screen_width_ // 2 - 100, self.screen_height_ // 2 - 50, 200, 50)
        self.medium_button_rect_ = pygame.Rect(self.screen_width_ // 2 - 100, self.screen_height_ // 2 + 50, 200, 50)
        self.hard_button_rect_ = pygame.Rect(self.screen_width_ // 2 - 100, self.screen_height_ // 2 + 150, 200, 50)
        self.input_rect_ = pygame.Rect(self.screen_width_ // 2 - 150, self.screen_height_ // 2 - 150, 300, 50)
        self.active_ = False
        self.input_color_active_ = constants.BLACK
        self.input_color_inactive_ = constants.LIGHT_GREY
        self.input_color_ = self.input_color_inactive_
        self.player_name_ = ''
        self.scores = scores

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

    def drawInputBox(self) -> None:
        # Draw input box
        pygame.draw.rect(self.screen_, self.input_color_, self.input_rect_, 2)
        text_surface = self.input_font_.render(self.player_name_, True, self.input_color_)
        self.screen_.blit(text_surface, (self.input_rect_.x + 5, self.input_rect_.y + 5))
        self.input_rect_.w = max(300, text_surface.get_width() + 10)

    def drawScores(self) -> None:
        margin = 70
        self.drawText("highscores", self.button_font_, constants.RED, self.screen_, self.screen_width_ - 150, 30)
        for i, (name, score) in enumerate(self.scores):
            y = margin + i * 40
            self.drawText(f"{name} : {score}", self.button_font_, constants.BLACK, self.screen_, self.screen_width_ - 150, y)


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
        self.drawScores()
        self.drawInputBox()
        pygame.display.update()

    def run(self) -> tuple:
        run = True
        difficulty = None
        while run:
            self.clock_.tick(constants.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_rect_.collidepoint(event.pos):
                        self.active_ = True
                    else:
                        self.active_ = False

                    self.input_color_ = self.input_color_active_ if self.active_ else self.input_color_inactive_

                    if self.easy_button_rect_.collidepoint(event.pos):
                        difficulty = 'easy'
                        run = False
                    elif self.medium_button_rect_.collidepoint(event.pos):
                        difficulty = 'medium'
                        run = False
                    elif self.hard_button_rect_.collidepoint(event.pos):
                        difficulty = 'hard'
                        run = False

                if event.type == pygame.KEYDOWN:
                    if self.active_:
                        if event.key == pygame.K_RETURN:
                            self.active_ = False
                            self.input_color_ = self.input_color_inactive_
                        elif event.key == pygame.K_BACKSPACE:
                            self.player_name_ = self.player_name_[:-1]
                        else:
                            self.player_name_ += event.unicode

            self.draw()
        
        return self.player_name_, difficulty