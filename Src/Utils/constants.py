#screen constants
rows = 15
cols = 20
tileSize = 48
fps = 60
PainelSize = 240
map_width = cols*tileSize
window = (((cols*tileSize)+ PainelSize), (rows*tileSize))

#draw rays
zapperQuant = 10
zapperRadius = 40

#game constants
levelMaxTower = 3
gold = 500
victory = 1000

#price towers
priceClassic = 75
priceDamage = 150
priceSplash = 200
priceSlow = 125

#enemys
bountyClassic = 30
bountyHealer = 50
bountyZapper = 30
bountyTank = 250
#healer
healRadius = 120
healAmount = 40
healInterval = 3


#projectile constants
projectileSpeed = 8

#cors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN_CHOC = (123, 63, 0)
BROWN_COFFEE = (75, 54, 33)
YELLOW = (255, 255, 0)
MUSTARD_YELLOW = (255, 219, 88)
RED = (255, 0, 0)
GREEN = (87, 128, 24)
GRAPHITE = (54, 69, 79)
SILVER = (192,192,192)
LIGHT_GREY = (211,211,211)

def setDificulty(dificult: str) -> None:
    global classicEnemySpeed, classicEnemyHealth, classicEnemyLifes ,healerSpeed, healerHealth, healerLifes ,tankSpeed, tankHealth, tankLifes ,zapperSpeed, zapperHealth, zapperLifes, zapperDuration
    
    if dificult == "easy":
        classicEnemySpeed = 1.7
        classicEnemyHealth = 130
        classicEnemyLifes = 1

        healerSpeed = 1.5
        healerHealth = 175
        healerLifes = 1

        tankSpeed = 1.5
        tankHealth = 700
        tankLifes = 1

        zapperSpeed = 3
        zapperHealth = 40
        zapperLifes = 2
        zapperDuration = 4

    elif dificult == "medium":
        classicEnemySpeed = 2.4
        classicEnemyHealth = 140
        classicEnemyLifes = 1

        healerSpeed = 1.8
        healerHealth = 200
        healerLifes = 1

        tankSpeed = 1.4
        tankHealth = 1200
        tankLifes = 5

        zapperSpeed = 4
        zapperHealth = 70
        zapperLifes = 3
        zapperDuration = 5

    elif dificult == "hard":
        classicEnemySpeed = 2.8
        classicEnemyHealth = 200
        classicEnemyLifes = 2

        healerSpeed = 2.2
        healerHealth = 300
        healerLifes = 2

        tankSpeed = 1.4
        tankHealth = 1500
        tankLifes = 8

        zapperSpeed = 5.5
        zapperHealth = 90
        zapperLifes = 4
        zapperDuration = 6


#constants animations
#enemy
ANIMATION_STEPS_ENEMY = 13
ANIMATION_STEPS_ENEMY_ZAPPER = 8
ANIMATION_STEPS_ENEMY_HEALER = 9
ANIMATION_STEPS_ENEMY_HEALER_SPECIAL = 9
ANIMATION_STEPS_ENEMY_TANK = 11
#tower
ANIMATION_STEPS_TOWER = 29
ANIMATION_STEPS_TOWER_SPLASH = 14

