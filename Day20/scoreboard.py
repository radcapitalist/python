
from turtle import Turtle
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

SCORE_FONT = "Courier New"
SCORE_ALIGN = "center"
SCORE_SIZE = 22
FNAME = "snake_high_score.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.init_high_score()
        self.setx(0)
        self.sety(270)
        self.color("white")
        self.hideturtle()
        self.display()

    def display(self):
        self.clear()
        self.write(arg = f"Score: {self.score}  High Score: {self.high_score}", \
                   align = SCORE_ALIGN, font=(SCORE_FONT, SCORE_SIZE, "normal"))

    def increment(self):
        self.score += 1
        self.display()

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.display()

    def reset(self):
        self.score = 0
        self.display()

    def init_high_score(self):
        if not os.path.exists(FNAME):
            with open(file = FNAME, mode = "w") as f:
                pass
            self.high_score = 0
        else:
            with open(file = FNAME) as f:
                self.high_score = int(f.read())

    def write_high_score(self):
        with open(file = FNAME, mode = "w") as f:
            f.write(f"{self.high_score}")