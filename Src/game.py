import pygame
import json
import sys
from Utils import constants
from Utils.side_menu import SideMenu
from Entities.tower import Tower
from Entities.enemy import Enemy

from Levels.levelLoader import Level

class Game():
    def __init__(self):
        pygame.init()

        self.gold_ = 1000
        
        self.clock_ = pygame.time.Clock()
        self.screen_ = pygame.display.set_mode(constants.window)
        pygame.display.set_caption("Defesa Blaster ")

        self.placing_tower = False
        
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
        self.buy_tower_Image_ = pygame.image.load("Assets/Sprites/Side_Menu/buy_turret.png").convert_alpha()
        self.cancelImage_ = pygame.image.load("Assets/Sprites/Side_Menu/cancel.png").convert_alpha()
        self.towerButton_ = SideMenu(constants.tileSize + 960, 120 , self.buy_tower_Image_, True)
        self.cancelButton_ = SideMenu(constants.tileSize + 960, 180, self.cancelImage_, True)
        

        enemy = Enemy(self.level_.waypoints_, self.enemyImage_,self.enemyDied)
        self.enemyGroup_.add(enemy)
        self.enemyCounter_ = 50
        self.projectileGroup_ = pygame.sprite.Group()

    def Run(self):
        run = True
        while (run):
            if self.enemyCounter_ == 0:
                self.spawnEnemy()
                self.enemyCounter_=50
            self.clock_.tick(constants.fps)

            self.Draw()
            self.enemyGroup_.update()
            self.projectileGroup_.update()
            self.towerGroup_.update(self.enemyGroup_,self.projectileGroup_) 
            self.enemyCounter_-=1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.Quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mousePos = pygame.mouse.get_pos()
                    if mousePos[0] <constants.window[0] and mousePos[1] < constants.window[1]:
                        if self.placing_tower == True:
                            action = self.CheckSpace(mousePos)
                            if action == 2:
                                self.CreateTurret(mousePos)
            if self.towerButton_.draw(self.screen_):
                self.placing_tower = True
            if self.placing_tower == True:
                self.cursor_rect = self.tower_.get_rect()
                self.cursor_pos = pygame.mouse.get_pos()
                self.cursor_rect.center = self.cursor_pos
                if self.cursor_pos[0] <= constants.tileSize:
                    self.screen_.blit(self.tower_, self.cursor_rect)
                if self.cancelButton_.draw(self.screen_):
                    self.placing_tower = False
            pygame.display.flip()

    def Quit(self):
        pygame.quit()

    def Draw(self):
        self.level_.draw(self.screen_)
        for tower in self.towerGroup_:
            tower.draw(self.screen_)
        self.enemyGroup_.draw(self.screen_)
        self.projectileGroup_.draw(self.screen_)
        
    def CreateTurret(self,pos):
        mousePosX = pos[0] // constants.tileSize
        mousePosY = pos[1] // constants.tileSize

        hasGold = True
        if self.gold_ <100:
            hasGold = False
        if hasGold: 
            tower = Tower(self.tower_,mousePosX,mousePosY )#,mousePosX,mousePosY )
            self.towerGroup_.add(tower)
            self.gold_ -=100

    def CheckSpace(self,pos)-> int: #Retorna 1 caso exista uma torre ,2 se o espaço é livre e 0 se esta na estrada
        mousePosX = pos[0] // constants.tileSize
        mousePosY = pos[1] // constants.tileSize
        self.mouse_tile_num = (mousePosY * constants.cols) + mousePosX
        for tower in self.towerGroup_: #tower é a torre especifica que foi clicada , sendo possivel retorna-la para upgrades
            if(mousePosX,mousePosY) == (tower.posX_,tower.posY_): #1 se já tem uma torre
                return 1 
        if self.level_.tilemap_[self.mouse_tile_num]  < 16: #2 se o espaço esta livre
            return 2
        else:
            return 0#0 se é rua
        
    def enemyDied(self, bounty):
        self.gold_ += bounty


    def spawnEnemy(self):
        enemy = Enemy(self.level_.waypoints_, self.enemyImage_,self.enemyDied)
        self.enemyGroup_.add(enemy)

            

        


