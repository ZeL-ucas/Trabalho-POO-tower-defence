import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game import Game
from Levels.startMenu import StartMenu



def main():
    menu = StartMenu()
    menu.run()
    TowerDefence = Game()
    TowerDefence.Run()
main() 