
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.setx(0)
        self.sety(270)
        self.color("white")
        self.display()

    def display(self):
        self.clear()
        self.write(arg = f"Score: {self.score}", align = "center", font=("Arial", 24, "normal"))

    def increment(self):
        self.score += 1
        self.display()

    def reset(self):
        self.score = 0
        self.display()

