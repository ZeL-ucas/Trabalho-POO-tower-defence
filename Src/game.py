import pygame
import json
import sys
from Utils import constants
from Utils.side_menu import SideMenu
from Entities.tower import Tower
from Entities.enemy import Enemy
from Entities.Enemys.healer import Healer
from Entities.Enemys.tank import Tank
from Entities.Enemys.frezzer import Frezzer
from Levels.levelLoader import Level
import time
class Game():
    def __init__(self)->None:
        pygame.init()

        self.gold_ = 1000
        self.font = pygame.font.SysFont(None, 36)
        self.clock_ = pygame.time.Clock()
        self.screen_ = pygame.display.set_mode(constants.window)
        pygame.display.set_caption("Defesa Blaster ")
        self.heart_image = pygame.image.load("Assets/Sprites/Icons/heart.png").convert_alpha()
        self.heart_image = pygame.transform.scale(self.heart_image, (24, 24))
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
    
        self.remainingLifes = 10

        self.projectileGroup_ = pygame.sprite.Group()
        self.waves = self.level_.loadWaves('Src/Utils/waves.txt')

        self.currentWaveIndex = 0

        self.currentWave = self.waves[self.currentWaveIndex] if self.waves else []
        self.enemyList = []
        self.lastSpawnTime = time.time()
        self.enemyTypes = {
            "Classic": self.createClassicEnemy,
            "Healer": self.createHealerEnemy,
            "Tank": self.createTankEnemy,
            "Frezzer": self.createFrezzerEnemy
        }

    def Run(self)->None:
        run = True

        while (run):
            self.clock_.tick(constants.fps)
            self.screen_.fill(constants.GRAPHITE)
            self.Draw()
            self.Update()
            if self.remainingLifes <=0:
                run = False
                self.Quit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.Quit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mousePos = pygame.mouse.get_pos()
                    if mousePos[0] <constants.map_width:
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
                if self.cursor_pos[0] <= constants.map_width:
                    self.screen_.blit(self.tower_, self.cursor_rect)
                if self.cancelButton_.draw(self.screen_):
                    self.placing_tower = False
            pygame.display.flip()

    def Quit(self)->None:
        pygame.quit()
        sys.exit()

    def Draw(self)->None:
        self.level_.draw(self.screen_)
        for tower in self.towerGroup_:
            tower.draw(self.screen_)
        self.enemyGroup_.draw(self.screen_)
        self.projectileGroup_.draw(self.screen_)

        gold_text = self.font.render(f"${self.gold_}", True, constants.YELLOW)  
        life_text = self.font.render(f"{self.remainingLifes}", True, constants.RED)
        waves_text = self.font.render(f"{self.currentWaveIndex}/{len(self.waves)}", True, constants.RED)
        self.screen_.blit(gold_text, (10, 10))
        self.screen_.blit(self.heart_image, (10, 50)) 
        self.screen_.blit(life_text, (40, 50))
        self.screen_.blit(waves_text, (10, 100))
        
    def CreateTurret(self,pos)->None:
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
        
    def EnemyDied(self, bounty,killed,lifes)->None:
        if not killed:
            self.remainingLifes-= lifes 
        self.gold_ += bounty


    def Waves(self)->None:
        current_time = time.time()

        if self.currentWave:
            count, enemy_type, delay = self.currentWave[0]

            if current_time - self.lastSpawnTime >= delay:
                self.SpawnEnemy(enemy_type)
                self.lastSpawnTime = current_time
                count -= 1

                if count > 0:
                    self.currentWave[0] = (count, enemy_type, delay)
                else:
                    self.currentWave.pop(0)

        elif len(self.enemyGroup_) == 0 and self.currentWaveIndex + 1 < len(self.waves):
            self.currentWaveIndex += 1
            self.currentWave = self.waves[self.currentWaveIndex]

    def SpawnEnemy(self, enemy_type)->None:
        if enemy_type in self.enemyTypes:
            create_enemy_func = self.enemyTypes[enemy_type]
            new_enemy = create_enemy_func()
            self.enemyGroup_.add(new_enemy)

    def createClassicEnemy(self)->Enemy:
        return Enemy(self.level_.waypoints_, self.enemyImage_, self.EnemyDied)

    def createHealerEnemy(self)->Healer:
        return Healer(self.level_.waypoints_, self.enemyGroup_, self.screen_, self.EnemyDied)

    def createTankEnemy(self)->Tank:
        return Tank(self.level_.waypoints_, self.EnemyDied)

    def createFrezzerEnemy(self)->Frezzer:
        return Frezzer(self.level_.waypoints_, self.towerGroup_, self.EnemyDied)
    
    def Update(self)->None:
        self.Waves()
        self.enemyGroup_.update()
        self.projectileGroup_.update()
        self.towerGroup_.update(self.enemyGroup_,self.projectileGroup_) 

        


