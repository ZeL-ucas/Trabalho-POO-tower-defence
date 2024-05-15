import pygame
import json
from Utils import constants
from Entities.tower import Tower
from Entities.enemy import Enemy
from Levels.levelLoader import Level
class Game():
    def __init__(self):
        pygame.init()

        self.gold_ = 1000
        
        self.clock_ = pygame.time.Clock()
        self.screen_ = pygame.display.set_mode(constants.window)
        pygame.display.set_caption("defesa blaster ")

        with open('Assets/Waypoints/mapa1.tmj') as file:
            self.level_data_ = json.load(file)
        self.tower_ = pygame.image.load("Assets/Sprites/Towers/towerTest.png").convert_alpha()
        self.tower_ = pygame.transform.scale(self.tower_, (48, 80)) #serve para mudar o tamanho da imagem (largura, altura)
        self.mapa_ = pygame.image.load("Assets/Backgrounds/mapa.png").convert_alpha()
        self.level_ = Level(self.level_data_, self.mapa_)
        self.towerGroup_ = pygame.sprite.Group()
        self.enemyImage_ = pygame.image.load("Assets/Sprites/Enemys/enemy_1.png").convert_alpha()
        self.enemyGroup_ = pygame.sprite.Group()
        self.level_.ProcessData()

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
                        self.CreateTurret(mousePos)
              
            pygame.display.flip()

    def Quit(self):
        pygame.quit()

    def Draw(self):
        self.level_.draw(self.screen_)
        self.towerGroup_.draw(self.screen_)
        self.enemyGroup_.draw(self.screen_)
        
    def CreateTurret(self,pos):
        mousePosX = pos[0] // constants.tileSize
        mousePosY = pos[1] // constants.tileSize
        spaceIsFree = True
        hasGold = True
        self.mouse_tile_num = (mousePosY * constants.cols) + mousePosX
        for tower in self.towerGroup_:
            if(mousePosX,mousePosY) == (tower.posX_,tower.posY_):
                spaceIsFree = False
        if self.gold_< 100:
            hasGold = False
        #checar se é grama
        if self.level_.tilemap_[self.mouse_tile_num] == 7:# ainda não esta 100% funcional, precisa verificar os valores do mapa
            if spaceIsFree and hasGold: 
                tower = Tower(self.tower_,mousePosX,mousePosY )#,mousePosX,mousePosY )
                self.towerGroup_.add(tower)
                self.gold_ -=100

            

        


