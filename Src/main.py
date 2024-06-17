import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game import Game
from Levels.startMenu import StartMenu
from Levels.endMenu import EndMenu
from Utils import constants


def main():
    run = True
    while(run):
        menu = StartMenu()
        dificulty = menu.run()
        constants.setDificulty(dificulty)
        towerDefence = Game()
        score = towerDefence.Run()
        towerDefence.Quit()
        if(score[0] == 'quit'):
            run = False
            sys.exit()
        gameEnd = EndMenu((score[0],score[1])) 
        choice = gameEnd.run()
        if choice == "quit":
            run = False
            sys.exit()
        



main() 