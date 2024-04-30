import pygame 
#from enemy import Enemy
#import constants as c

#initialise pygame  
pygame.init()

#create clock 
Clock = pygame.time.Clock()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FPS = 60

#create game window  
#sreen.pg.display.set_mode((width 500 pixels, height 500 pixels ))
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("TOWER DEFENCE")

#load image
#enemy_image = pygame.image.load()

#create group:
#enemy_group = pygame.sprite.Group()

#enemy = Enemy((200,300), enemy_image)
#enemy_group.add(enemy)

#game loop
run = True
while run: 
    
  Clock.tick(FPS)

  #without a trace
  screen.fill("gray100")

  #update groups
  #enemy_group.update()

  #draw groups
  #enemy_group.draw(screen)

  #event handler
  for event in pygame.event.get():
    #quit program
    if event.type == pygame.QUIT:
      run = False

#upgrade display
#pygame.display.flip()
      
pygame.quit()