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

    while(run):
        data = DataBase("Src/Utils/highscores.txt")
        currentScores = data.GetHighScores()

        menu = StartMenu(currentScores)
        currentPlayerData = menu.run()
        constants.setDificulty(currentPlayerData[1])
        towerDefence = Game()
        score = towerDefence.Run()
        scoreText=score[1]
        if currentPlayerData[1] == "easy":
            scoreText *= 0.8
        elif currentPlayerData[1] == "hard":
            scoreText *= 1.2
        towerDefence.Quit()
        if(score[0] == 'quit'):
            run = False
            sys.exit()
        
        gameEnd = EndMenu(score[0],str(scoreText))
        choice = gameEnd.run()
        data.AddHighScore(currentPlayerData[0],int(scoreText))
        if choice == "quit":
            run = False
            sys.exit()

        



main() 