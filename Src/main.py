import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game import Game
from Levels.startMenu import StartMenu
from Utils import constants


def main():
    run = True
    while(run):
        menu = StartMenu()
        dificulty = menu.run()
        constants.setDificulty(dificulty)
        TowerDefence = Game()
        score = TowerDefence.Run()
        print(score)
        TowerDefence.Quit()
        print(score[0])
        print(score)
        if(score[0] == 'quit'):
            run = False
            sys.exit()


main() 