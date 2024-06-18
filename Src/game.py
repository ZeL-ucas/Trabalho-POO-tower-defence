import pygame
import json
import sys
import math
from Utils import constants
from Src.Utils.sideMenu import SideMenu
from Entities.tower import Tower
from Entities.Towers.towerDamage import TowerDamage
from Entities.Towers.towerSplash import TowerSplash
from Entities.enemy import Enemy
from Entities.Enemys.healer import Healer
from Entities.Enemys.tank import Tank
from Entities.Enemys.zapper import Zapper
from Levels.levelLoader import Level
import time
from Utils.towerMenu import TowerMenu

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
        self.is_select_ = False
        self.tower_menu = None

        with open('Assets/Waypoints/mapa1.tmj') as file:
            self.level_data_ = json.load(file)
        self.tower_ = pygame.image.load("Assets/Sprites/Towers/TowerClassic/towerClassic.png").convert_alpha()
        self.tower_ = pygame.transform.scale(self.tower_, (48, 80))
        self.mapa_ = pygame.image.load("Assets/Backgrounds/mapa.png").convert_alpha()
        self.level_ = Level(self.level_data_, self.mapa_)
        self.towerGroup_ = pygame.sprite.Group()
        self.enemyImage_ = pygame.image.load("Assets/Sprites/Enemys/EnemyClassic/enemy_classic.png").convert_alpha()
        self.enemyGroup_ = pygame.sprite.Group()
        self.level_.ProcessData()
        self.buy_tower_Image_ = pygame.image.load("Assets/Sprites/Side_Menu/buy_turret.png").convert_alpha()
        self.cancelImage_ = pygame.image.load("Assets/Sprites/Side_Menu/cancel.png").convert_alpha()
        self.upgradeImage_ = pygame.image.load("Assets/Sprites/TowerMenu/upgrade_icon.svg").convert_alpha()
        self.towerButton_ = SideMenu(constants.tileSize + 960, 120, self.buy_tower_Image_, True)
        self.cancelButton_ = SideMenu(constants.tileSize + 960, 180, self.cancelImage_, True)

        self.remainingLifes = 10

        self.projectileGroup_ = pygame.sprite.Group()
        self.waves = self.level_.loadWaves('Src/Utils/waves.txt')

        self.currentWaveIndex = 0

        self.currentWave = self.waves[self.currentWaveIndex] if self.waves else []
        self.enemyList = []
        self.lastSpawnTime = time.time()
        self.enemyTypes = {
            "Classic": self.CreateClassicEnemy,
            "Healer": self.CreateHealerEnemy,
            "Tank": self.CreateTankEnemy,
            "Zapper": self.CreateZapperEnemy
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
                    if self.tower_menu and self.tower_menu.is_clicked(mousePos):
                        self.UpgradeTower(self.tower_menu.tower)
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
            if self.placing_tower:
                self.cursor_rect = self.tower_.get_rect()
                self.cursor_pos = pygame.mouse.get_pos()
                self.cursor_rect.center = self.cursor_pos
                if self.cursor_pos[0] <= constants.map_width:
                    self.screen_.blit(self.tower_, self.cursor_rect)
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
        sys.exit()

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
        waves_text = self.font.render(f"{self.currentWaveIndex}/{len(self.waves)}", True, constants.RED)
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
        if self.gold_ < 100:
            hasGold = False
        if hasGold: 
            tower = TowerSplash( mousePosX, mousePosY)
            self.towerGroup_.add(tower)
            self.gold_ -= 100

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
        self.tower_menu = TowerMenu(tower, self.screen_, self.upgradeImage_)

    def EnemyDied(self, bounty:int,killed:bool,lifes:int)->None:
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

    def SpawnEnemy(self, enemy_type:str)->None:
        if enemy_type in self.enemyTypes:
            create_enemy_func = self.enemyTypes[enemy_type]
            new_enemy = create_enemy_func()
            self.enemyGroup_.add(new_enemy)

    def CreateClassicEnemy(self)->Enemy:
        return Enemy(self.level_.waypoints_,13, self.enemyImage_, self.EnemyDied)

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