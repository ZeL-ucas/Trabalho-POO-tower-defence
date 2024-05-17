import pygame
import json
from Utils import constants
from Utils.side_menu import SideMenu
from Entities.tower import Tower
from Entities.enemy import Enemy
from Levels.levelLoader import Level

class Game():
    def __init__(self):
        pygame.init()

        self.gold_ = 500
        
        self.clock_ = pygame.time.Clock()
        self.screen_ = pygame.display.set_mode(constants.window)
        pygame.display.set_caption("defesa blaster ")

        self.placing_tower = False
        
        with open('Assets/Waypoints/mapa1.tmj') as file:
            self.level_data_ = json.load(file)
        self.tower_ = pygame.image.load("Assets/Sprites/Towers/cursor_turret.png").convert_alpha()
        self.mapa_ = pygame.image.load("Assets/Backgrounds/mapa.png").convert_alpha()
        self.level_ = Level(self.level_data_, self.mapa_)
        self.towerGroup_ = pygame.sprite.Group()
        self.enemyImage_ = pygame.image.load("Assets/Sprites/Enemys/enemy_1.png").convert_alpha()
        self.enemyGroup_ = pygame.sprite.Group()
        self.level_.ProcessData()
        self.buy_tower_Image_ = pygame.image.load("Assets/Sprites/Side_Menu/buy_turret.png").convert_alpha()
        self.cancelImage_ = pygame.image.load("Assets/Sprites/Side_Menu/cancel.png").convert_alpha()
        self.towerButton_ = SideMenu(constants.tileSize + 30, 120 , self.buy_tower_Image_, True)
        self.cancelButton_ = SideMenu(constants.tileSize + 50, 180, self.cancelImage_, True)
        

        enemy = Enemy(self.level_.waypoints_, self.enemyImage_)
        self.enemyGroup_.add(enemy)

    def Run(self):
        run = True
        while (run):

            self.clock_.tick(constants.fps)

            self.Draw()
            self.enemyGroup_.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.Quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mousePos = pygame.mouse.get_pos()
                    if mousePos[0] <constants.window[0] and mousePos[1] <constants.window[1]:
                        if self.placing_tower == True:
                            self.CreateTurret(mousePos)
            if self.towerButton_.draw(self.screen_):
                self.placing_tower = True
            if self.placing_tower == True:
                if self.cancelButton_.draw(self.screen_):
                    self.placing_tower = False
            pygame.display.flip()

    def Quit(self):
        pygame.quit()

    def Draw(self):
        self.level_.draw(self.screen_)
        self.towerGroup_.draw(self.screen_)
        self.enemyGroup_.draw(self.screen_)
        
    def CreateTurret(self,pos):
        mousePosX = pos[0] #/ constante.tileSize
        mousePosY = pos[1] #/ constante.tileSize
        spaceIsFree = True
        hasGold = True
        for tower in self.towerGroup_:
            if(mousePosX,mousePosY) == (tower.posX_,tower.posY_):
                spaceIsFree = False
        if self.gold_< 100:
            hasGold = False
        if spaceIsFree and hasGold: 
            tower = Tower(self.tower_,mousePosX,mousePosY )#,mousePosX,mousePosY )
            self.towerGroup_.add(tower)
            self.gold_ -=100
        


