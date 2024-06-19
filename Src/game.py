import pygame
import json
import sys
import math
from Utils import constants
from Src.Utils.sideMenu import SideMenu
from Entities.tower import Tower
from Entities.Towers.towerDamage import TowerDamage
from Entities.Towers.towerSplash import TowerSplash
from Entities.Towers.towerSlow import TowerSlow
from Entities.enemy import Enemy
from Entities.Enemys.healer import Healer
from Entities.Enemys.tank import Tank
from Entities.Enemys.zapper import Zapper
from Levels.levelLoader import Level
import time
from Utils.towerMenu import TowerMenu
from Interfaces.gameInterface import InterfaceGame
class Game(InterfaceGame):
    def __init__(self)->None:
        pygame.init()

        self.font = pygame.font.SysFont(None, 36)
        self.clock_ = pygame.time.Clock()
        self.screen_ = pygame.display.set_mode(constants.window)
        pygame.display.set_caption("Defesa Blaster ")

        with open('Assets/Waypoints/mapa1.tmj') as file:
            self.level_data_ = json.load(file)

        self.tower_ = {
            "Classic": pygame.transform.scale(pygame.image.load("Assets/Sprites/Towers/TowerClassic/towerClassic.png").convert_alpha(), (48, 80)),
            "Damage": pygame.transform.scale(pygame.image.load("Assets/Sprites/Towers/TowerDamage/towerDamage.png").convert_alpha(), (48, 80)),
            "Splash": pygame.image.load("Assets/Sprites/Towers/TowerSplash/towerSplashImage.png").convert_alpha(),
            "Slow": pygame.transform.scale(pygame.image.load("Assets/Sprites/Towers/TowerDamage/towerDamage.png").convert_alpha(), (48, 80))
        }

        self.enemyTypes = {
            "Classic": self.CreateClassicEnemy,
            "Healer": self.CreateHealerEnemy,
            "Tank": self.CreateTankEnemy,
            "Zapper": self.CreateZapperEnemy
        }

        self.heart_image = pygame.image.load("Assets/Sprites/Icons/heart.png").convert_alpha()
        self.heart_image = pygame.transform.scale(self.heart_image, (24, 24))
        self.mapa_ = pygame.image.load("Assets/Backgrounds/mapa.png").convert_alpha()
        self.cancelImage_ = pygame.image.load("Assets/Sprites/Side_Menu/cancel.png").convert_alpha()
        self.enemyImage_ = pygame.image.load("Assets/Sprites/Enemys/EnemyClassic/enemy_classic.png").convert_alpha()


        self.level_ = Level(self.level_data_, self.mapa_)
        self.level_.ProcessData()

        self.towerButton_ = SideMenu(constants.tileSize + 950, 20, self.tower_["Classic"], True)
        self.towerButtonDamage = SideMenu(constants.tileSize + 1070, 20, self.tower_["Damage"], True)
        self.towerButtonSplash = SideMenu(constants.tileSize + 950, 100, self.tower_["Splash"], True)
        self.towerButtonSlow = SideMenu(constants.tileSize + 1070, 100, self.tower_["Slow"], True)
        self.cancelButton_ = SideMenu(constants.tileSize + 950, 240, self.cancelImage_, True)

        self.towerGroup_ = pygame.sprite.Group()
        self.enemyGroup_ = pygame.sprite.Group()
        self.projectileGroup_ = pygame.sprite.Group()
        self.waves = self.level_.loadWaves('Src/Utils/waves.txt')
        self.lastSpawnTime = time.time()
        self.currentWaveIndex = 0
        self.currentWave = self.waves[self.currentWaveIndex] if self.waves else []
        self.score =0 
        self.remainingLifes = 10
        self.enemyList = []
        self.gold_ = constants.gold
        self.won = False
        self.placing_tower = False
        self.is_select_ = False
        self.tower_menu = None


    def Run(self)->int:
        run = True

        while (run):
            self.clock_.tick(constants.fps)
            self.screen_.fill(constants.GRAPHITE)
            self.Draw()
            self.Update()

            #checando derrota
            if self.remainingLifes <=0:
                run = False
                return "lose",self.score
            #checando vitoria
            if self.won:
                self.score += constants.victory
                return "win",self.score

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    return "quit",self.score

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mousePos = pygame.mouse.get_pos()
                    if self.tower_menu and self.tower_menu.is_clicked(mousePos) == "upgrade":
                        self.UpgradeTower(self.tower_menu.tower)
                        self.tower_menu = None
                    elif self.tower_menu and self.tower_menu.is_clicked(mousePos) == "sell":
                        self.SellTower(self.tower_menu.tower)
                        self.tower_menu = None
                    elif self.isClickOutsideMenu(mousePos):
                        self.tower_menu = None
                    else:
                        if mousePos[0] < constants.map_width:
                            action = self.CheckSpace(mousePos)
                            if self.placing_tower and action == 2:
                                self.CreateTurret(mousePos)
            if self.towerButton_.draw(self.screen_):
                self.placing_tower = True
                self.towerType = "Classic"
            if self.towerButtonDamage.draw(self.screen_):
                self.placing_tower = True
                self.towerType = "Damage"
            if self.towerButtonSplash.draw(self.screen_):
                self.placing_tower = True
                self.towerType = "Splash"
            if self.towerButtonSlow.draw(self.screen_):
                self.placing_tower = True
                self.towerType = "Slow"

            if self.placing_tower:
                tower_image = self.tower_[self.towerType]
                self.cursor_rect =tower_image.get_rect()
                self.cursor_pos = pygame.mouse.get_pos()
                self.cursor_rect.center = self.cursor_pos
                if self.cursor_pos[0] <= constants.map_width:
                    self.screen_.blit(tower_image, self.cursor_rect)
                if self.cancelButton_.draw(self.screen_):
                    self.placing_tower = False
            if self.tower_menu:
                self.tower_menu.draw()
            pygame.display.flip()

    def Quit(self) -> None:
        """
        Encerra o Pygame e fecha o jogo.
        """
        pygame.quit()


    def Draw(self) -> None:
        """
        Desenha todos os elementos do jogo na tela.
        """
        self.level_.draw(self.screen_)
        self.towerGroup_.draw(self.screen_)
        self.enemyGroup_.draw(self.screen_)
        self.projectileGroup_.draw(self.screen_)

        gold_text = self.font.render(f"${self.gold_}", True, constants.YELLOW)  
        life_text = self.font.render(f"{self.remainingLifes}", True, constants.RED)
        waves_text = self.font.render(f"{self.currentWaveIndex+1}/{len(self.waves)}", True, constants.RED)
        self.screen_.blit(gold_text, (10, 10))
        self.screen_.blit(self.heart_image, (10, 50)) 
        self.screen_.blit(life_text, (40, 50))
        self.screen_.blit(waves_text, (10, 100))
        
    def CreateTurret(self, pos:tuple) -> None:
        """
        Cria uma torre na posição especificada se o jogador tiver ouro suficiente.
        
        Observação: A variável "pos" é a coordenada X,Y. 
        """
        mousePosX = pos[0] // constants.tileSize
        mousePosY = pos[1] // constants.tileSize

        hasGold = True
        if self.gold_ < constants.priceClassic:
            hasGold = False
        if hasGold:
            if self.towerType == "Classic":
                tower = Tower(self.tower_[self.towerType], mousePosX, mousePosY)
            elif self.towerType == "Damage":
                tower = TowerDamage(mousePosX, mousePosY)
            elif self.towerType == "Splash":
                tower = TowerSplash( mousePosX, mousePosY)
            elif self.towerType == "Slow":
                tower = TowerSlow( mousePosX, mousePosY)
            self.towerGroup_.add(tower)
            self.gold_ -= tower.price

    def CheckSpace(self, pos:tuple) -> int:
        """
        Verifica se o espaço especificado está disponível para colocar uma torre.
        Retorna:
            1 se o espaço já está ocupado por uma torre.
            2 se o espaço está disponível.
            0 se o espaço não é válido.
        """
        mousePosX = pos[0] // constants.tileSize
        mousePosY = pos[1] // constants.tileSize
        self.mouse_tile_num = (mousePosY * constants.cols) + mousePosX
        for tower in self.towerGroup_:
            if (mousePosX, mousePosY) == (tower.posX_, tower.posY_):
                self.menuTower(tower)
                self.is_select_ = True
                return 1
        if self.level_.tilemap_[self.mouse_tile_num] < 16:
            return 2
        else:
            return 0
        
    def menuTower(self, tower:Tower) -> None:
        """
        Mostra o menu de upgrade para a torre especificada.
        """
        tower.drawRange(self.screen_)
        self.tower_menu = TowerMenu(tower, self.screen_)

    def EnemyDied(self, bounty:int,killed:bool,lifes:int)->None:
        if killed:
            self.score += bounty*0.8
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

        elif len(self.enemyGroup_) == 0:
            if self.currentWaveIndex + 1 < len(self.waves):
                self.score += 500
                self.currentWaveIndex += 1
                self.currentWave = self.waves[self.currentWaveIndex]
            elif self.currentWaveIndex + 1 == len(self.waves):
                self.won =True

    def SpawnEnemy(self, enemy_type:str)->None:
        if enemy_type in self.enemyTypes:
            create_enemy_func = self.enemyTypes[enemy_type]
            new_enemy = create_enemy_func()
            self.enemyGroup_.add(new_enemy)

    def CreateClassicEnemy(self)->Enemy:
        return Enemy(self.level_.waypoints_,13, self.enemyImage_, "classic", self.EnemyDied)

    def CreateHealerEnemy(self)->Healer:
        return Healer(self.level_.waypoints_, self.enemyGroup_, self.screen_, self.EnemyDied)

    def CreateTankEnemy(self)->Tank:
        return Tank(self.level_.waypoints_, self.EnemyDied)

    def CreateZapperEnemy(self)->Zapper:
        return Zapper(self.level_.waypoints_, self.towerGroup_, self.EnemyDied)
    
    def Update(self)->None:
        self.Waves()
        self.enemyGroup_.update()
        self.projectileGroup_.update()
        self.towerGroup_.update(self.enemyGroup_,self.projectileGroup_,self.screen_) 

        

    def isClickOutsideMenu(self, mouse_pos:tuple) -> bool:
        """
        Verifica se um clique do mouse está fora do menu de upgrade da torre.
        """
        if self.tower_menu:
            tower_pos = self.tower_menu.tower.getPosition()
            radius = self.tower_menu.radius
            distance = math.hypot(mouse_pos[0] - tower_pos[0], mouse_pos[1] - tower_pos[1])
            return distance > radius
        return False

    def UpgradeTower(self, tower:Tower) -> None:
        """
        Realiza o upgrade da torre se o jogador tiver ouro suficiente.
        """
        if self.gold_ >= self.tower_menu.tower.upcost_ and self.tower_menu.tower.upgrade_level_ < constants.levelMaxTower:
            self.gold_ -= self.tower_menu.tower.upcost_
            tower.upgrade()   
    def SellTower(self,tower:Tower)->None:
        self.gold_ += (tower.price / 2) * tower.upgrade_level_ 
        tower.kill()

