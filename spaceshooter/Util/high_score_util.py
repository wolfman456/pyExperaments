import datetime

PATH = "/home/bloodwolf/project/python/pyExperaments/spaceshooter/resources/high_scores.txt"


class HighScore:
    def __init__(self):
        self.player_name = None
        self.score = None
        self.date = datetime.datetime.today().strftime("%d/%m/%Y")
        self.high_scores = []

    def save(self):
        try:
            new_score = (self.player_name, self.score, self.date)
            self.high_scores.append(new_score)
            with open(PATH, "a") as high_scores_file:
                for score in self.high_scores:
                    high_scores_file.write(str(score) + "\n")
                high_scores_file.close()
        except (FileNotFoundError, RuntimeError) as x:
            print("error writing high scores" + str(x))

    def get_high_score(self):
        try:
            with open(PATH, 'r') as file:
                lines = file.readlines()
                high_score = [tuple(line.strip('(').strip(')').strip(',').split()) for line in lines]
                self.high_scores.append(high_score)
                print(self.high_scores[0][2])
        except (FileNotFoundError, RuntimeError) as x:
            print("error reading high scores" + str(x))
