import pygame 
from Entities.enemy import Enemy
import Entities.constants as c
 

#initialise pygame  
pygame.init()

#create clock 
clock = pygame.time.Clock()

#create game window  
#sreen.pg.display.set_mode((width 500 pixels, height 500 pixels ))
screen = pygame.display.set_mode((c.SCREEN_WIDTH,c.SCREEN_HEIGHT))
pygame.display.set_caption("TOWER DEFENCE")

#load image
#map
#map_image = pygame.image.load('Src/Levels/mapa_TD.png').convert_alpha()
#enemies
enemy_image = pygame.image.load('assets/sprites/enemys/enemy_1.png').convert_alpha()

#create group:
enemy_group = pygame.sprite.Group()

waypoints = [
  (100,100),
  (400,200),
  (400,100),
  (200,300)
]
enemy = Enemy(waypoints, enemy_image)
enemy_group.add(enemy)

#game loop
run = True
while run: 
    
  clock.tick(c.FPS)

  #without a trace
  screen.fill("gray100")

  #draw enemy path
  pygame.draw.lines(screen, "gray0", False, waypoints)

  #update groups
  enemy_group.update()

  for enemy in enemy_group:
    enemy.move()

  #draw groups
  enemy_group.draw(screen)

  #event handler
  for event in pygame.event.get():
    #quit program
    if event.type == pygame.QUIT:
      run = False

  #upgrade display
  pygame.display.flip()
      
pygame.quit()