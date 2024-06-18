
class DataBase():
    def __init__(self,path) -> None:
        self.path = path
        self.scores = None
        pass
    def ReadHighScores(self):
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                scores = file.readlines()
                return scores
        except FileNotFoundError:
            print(f"The file {self.caminho_arquivo} could not be found.")
        except IOError:
            print(f"There has been an error reading {self.caminho_arquivo}.")

    def GetHighScores(self):
        scores = self.ReadHighScores()
        highscores = []
        for line in scores:
            try:
                name, score = line.strip().split()
                score = int(score)
                highscores.append((name, score))
            except ValueError:
                print(f"error on line : {line.strip()}")
                continue

        highscores.sort(key=lambda x: x[1], reverse=True)

        return highscores
    
    def AddHighScore(self, newName, newScore):
        highscores = self.GetHighScores()
        
        hasHighscore = False
        for i, (name, score) in enumerate(highscores):
            if newName == name:
                hasHighscore = True
                if newScore > score:
                    highscores[i] = (newName, newScore)
                break

        if not hasHighscore:
            if len(highscores) < 5 or newScore > highscores[-1][1]:
                highscores.append((newName, newScore))
                highscores.sort(key=lambda x: x[1], reverse=True)
                highscores = highscores[:5]

        try:
            with open(self.path, 'w', encoding='utf-8') as file:
                for name, score in highscores:
                    file.write(f"{name} {score}\n")
        except IOError:
            print(f"There has been an error writing to {self.path}.")