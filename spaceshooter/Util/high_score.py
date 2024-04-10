import datetime

PATH = "/home/bloodwolf/project/python/pyExperaments/spaceshooter/resources/high_scores.txt"


class HighScore:
    def __init__(self):
        self.player_name = None
        self.score = None
        self.date = None
        self.high_scores = []

    def save(self):
        self.player_name = "bob"
        test = (self.player_name, 4, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        test1 = ("bob", 4, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.high_scores.append(test)
        self.high_scores.append(test1)
        try:

            with open(PATH, "a") as high_scores_file:
                for score in self.high_scores:
                    high_scores_file.write(str(score) + "\n")
                high_scores_file.close()
        except (FileNotFoundError, RuntimeError) as x:
            print("error writing high scores" + str(x))

    def get_high_score(self):
        with open(PATH, 'r') as file:
            line = file.read().splitlines()
            print(line)


high_score = HighScore()
high_score.save()
