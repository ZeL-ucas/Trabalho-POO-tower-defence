import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game import Game
from Levels.startMenu import StartMenu
from Levels.endMenu import EndMenu
from Utils.dataBase import DataBase
from Utils import constants


def main():
    run = True
    data = DataBase("/home/jose/POO/Trabalho-POO-tower-defence/Src/Utils/highscores.txt")
    data.AddHighScore("breno",1200)
    print(data.GetHighScores())
    
    # while(run):
    #     menu = StartMenu()
    #     dificulty = menu.run()
    #     constants.setDificulty(dificulty)
    #     towerDefence = Game()
    #     score = towerDefence.Run()
    #     scoreText=0
    #     if dificulty == "easy":
    #         scoreText = score[1] *0.8
    #     elif dificulty == "hard":
    #         scoreText = score[1] *1.2
    #     towerDefence.Quit()

    #     if(score[0] == 'quit'):
    #         run = False
    #         sys.exit()
        
    #     gameEnd = EndMenu(score[0],str(scoreText))
    #     choice = gameEnd.run()
    #     if choice == "quit":
    #         run = False
    #         sys.exit()
        



main() 