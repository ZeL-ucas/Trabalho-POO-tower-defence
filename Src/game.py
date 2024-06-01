import pygame
import json
import sys
import math
from Utils import constants
from Utils.side_menu import SideMenu
from Entities.tower import Tower
from Entities.enemy import Enemy
from Levels.levelLoader import Level
from Utils.towerMenu import TowerMenu

class Game():
    def __init__(self) -> None:
        """
        Inicializa a instância do jogo, configura a tela, carrega os recursos
        e inicializa os grupos de sprites.
        """
        pygame.init()

        self.gold_ = 1000
        
        self.clock_ = pygame.time.Clock()
        self.screen_ = pygame.display.set_mode(constants.window)
        pygame.display.set_caption("Defesa Blaster ")

        self.placing_tower = False
        self.is_select_ = False
        self.tower_menu = None

        with open('Assets/Waypoints/mapa1.tmj') as file:
            self.level_data_ = json.load(file)
        self.tower_ = pygame.image.load("Assets/Sprites/Towers/towerTest.png").convert_alpha()
        self.tower_ = pygame.transform.scale(self.tower_, (48, 80))
        self.mapa_ = pygame.image.load("Assets/Backgrounds/mapa.png").convert_alpha()
        self.level_ = Level(self.level_data_, self.mapa_)
        self.towerGroup_ = pygame.sprite.Group()
        self.enemyImage_ = pygame.image.load("Assets/Sprites/Enemys/enemy_1.png").convert_alpha()
        self.enemyGroup_ = pygame.sprite.Group()
        self.level_.ProcessData()
        self.buy_tower_Image_ = pygame.image.load("Assets/Sprites/Side_Menu/buy_turret.png").convert_alpha()
        self.cancelImage_ = pygame.image.load("Assets/Sprites/Side_Menu/cancel.png").convert_alpha()
        self.upgradeImage_ = pygame.image.load("Assets/Sprites/TowerMenu/upgrade_icon.svg").convert_alpha()
        self.towerButton_ = SideMenu(constants.tileSize + 960, 120, self.buy_tower_Image_, True)
        self.cancelButton_ = SideMenu(constants.tileSize + 960, 180, self.cancelImage_, True)

        enemy = Enemy(self.level_.waypoints_, self.enemyImage_, self.enemyDied)
        self.enemyGroup_.add(enemy)
        self.enemyCounter_ = 50
        self.projectileGroup_ = pygame.sprite.Group()

    def Run(self) -> None:
        """
        Inicia o loop principal do jogo.
        """
        run = True
        while run:
            if self.enemyCounter_ == 0:
                self.spawnEnemy()
                self.enemyCounter_ = 50
            self.clock_.tick(constants.fps)
            self.screen_.fill(constants.GRAPHITE)
            self.Draw()
            self.enemyGroup_.update()
            self.projectileGroup_.update()
            self.towerGroup_.update(self.enemyGroup_, self.projectileGroup_) 
            self.enemyCounter_ -= 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.Quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mousePos = pygame.mouse.get_pos()
                    if self.tower_menu and self.tower_menu.is_clicked(mousePos):
                        self.UpgradeTower(self.tower_menu.tower)
                        self.tower_menu = None
                    elif self.is_click_outside_menu(mousePos):
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

    def Draw(self) -> None:
        """
        Desenha todos os elementos do jogo na tela.
        """
        self.level_.draw(self.screen_)
        self.towerGroup_.draw(self.screen_)
        self.enemyGroup_.draw(self.screen_)
        self.projectileGroup_.draw(self.screen_)
        
    def CreateTurret(self, pos:list) -> None:
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
            tower = Tower(self.tower_, mousePosX, mousePosY)
            self.towerGroup_.add(tower)
            self.gold_ -= 100

    def CheckSpace(self, pos:list) -> int:
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

    def enemyDied(self, bounty: int) -> None:
        """
        Incrementa a quantidade de ouro do jogador quando um inimigo é derrotado.
        """
        self.gold_ += bounty

    def spawnEnemy(self) -> None:
        """
        Cria um novo inimigo e adiciona ao grupo de inimigos.
        """
        enemy = Enemy(self.level_.waypoints_, self.enemyImage_, self.enemyDied)
        self.enemyGroup_.add(enemy)

    def menuTower(self, tower:Tower) -> None:
        """
        Mostra o menu de upgrade para a torre especificada.
        """
        tower.drawRange(self.screen_)
        self.tower_menu = TowerMenu(tower, self.screen_, self.upgradeImage_)


    def is_click_outside_menu(self, mouse_pos:float) -> bool:
        """
        Verifica se um clique do mouse está fora do menu de upgrade da torre.
        """
        if self.tower_menu:
            tower_pos = self.tower_menu.tower.get_position()
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