
from turtle import Turtle

SCORE_FONT = "Courier New"
SCORE_ALIGN = "center"
SCORE_SIZE = 22

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
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
        self.display()

    def reset(self):
        self.score = 0
        self.display()

