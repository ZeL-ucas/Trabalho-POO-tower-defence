


rows = 15
cols = 20
tileSize = 48
fps = 60
PainelSize = 240
map_width = cols*tileSize
window = (((cols*tileSize)+ PainelSize), (rows*tileSize))
#classic
classicEnemySpeed = 2
classicEnemyHealth = 100
classicEnemyLifes = 1
#healer
healerSpeed = 0.75
healerHealth = 150
healerLifes = 1 
#tank
tankSpeed = 1.3
tankHealth = 500
tankLifes= 1 
#frezzer
frezzerSpeed = 4
frezzerHealth = 40
frezzerLifes= 2
freezeDuration = 4

levelMaxTower = 3
#cores
BLACK = (0, 0, 0)
BROWN_CHOC = (123, 63, 0)
BROWN_COFFEE = (75, 54, 33)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (87, 128, 24)
GRAPHITE = (54, 69, 79)
SILVER = (192,192,192)
LIGHT_GREY = (211,211,211)
def setDificulty(dificult:str)->None:  
    global classicEnemySpeed, classicEnemyHealth, classicEnemyLifes
    global healerSpeed, healerHealth, healerLifes
    global tankSpeed, tankHealth, tankLifes
    global frezzerSpeed, frezzerHealth, frezzerLifes, freezeDuration
    
    if dificult == "medium":
        classicEnemySpeed = 2.5
        classicEnemyHealth = 10
        classicEnemyLifes = 1
        
        healerSpeed = 1
        healerHealth = 175
        healerLifes = 1
        
        tankSpeed = 1.3
        tankHealth = 650
        tankLifes = 2
        
        frezzerSpeed = 4.5
        frezzerHealth = 40
        frezzerLifes = 3
        freezeDuration = 5
    
    elif dificult == "hard":
        classicEnemySpeed = 2.7
        classicEnemyHealth = 160
        classicEnemyLifes = 1
        
        healerSpeed = 1.25
        healerHealth = 250
        healerLifes = 2
        
        tankSpeed = 1
        tankHealth = 1000
        tankLifes = 3
        
        frezzerSpeed = 6
        frezzerHealth = 50
        frezzerLifes = 4
        freezeDuration = 7
