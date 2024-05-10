

import pygame
from Utils import constants
from Entities.tower import Tower
from Entities.enemy import Enemy
class Game():
    def __init__(self):
        pygame.init()

        self.gold_ = 500
        
        self.clock_ = pygame.time.Clock()
        self.screen_ = pygame.display.set_mode(constants.window)
        pygame.display.set_caption("defesa blaster ")

        self.tower_ = pygame.image.load("Assets/Sprites/Towers/cursor_turret.png").convert_alpha()
        self.mapa_ = pygame.image.load("Assets/Backgrounds/mapa.png").convert_alpha()
        self.towerGroup_ = pygame.sprite.Group()
        self.enemyImage_ = pygame.image.load("Assets/Sprites/Enemys/enemy_1.png").convert_alpha()
        self.enemyGroup_ = pygame.sprite.Group()
        waypoints = [
          (100,100),
          (400,200),
          (400,100),
          (200,300)
        ]
        enemy = Enemy(waypoints, self.enemyImage_)
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
                        self.CreateTurret(mousePos)
              
            pygame.display.flip()

    def Quit(self):
        pygame.quit()

    def Draw(self):
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


