
from turtle import Turtle, Screen
from random import choice

screen = Screen()
screen.setup(width=500, height=400)
screen.setworldcoordinates(0, 0, 500, 400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

bet_on = ""
while not bet_on in colors:
    bet_on = screen.textinput(title="Make your Bet", prompt="Which turtle will win the race? Enter a color.")

class RacingTurtle:
    def __init__(self, n, color):
        self._n = n
        self._color = color
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.hideturtle()
        self.turtle.speed(8)
        self.turtle.shape("turtle")
        self.turtle.color(self._color)
        self.turtle.goto(250, 200)
        self.turtle.showturtle()
        self.turtle.speed(5)

    def move_to_start(self):
        self.turtle.goto(5, 80 + (50 * self._n))

    def advance(self):
        self.turtle.forward(10)
        return self.turtle.xcor() > 480
    
    def get_color(self):
        return self._color

turtles = []
for i in range(0, len(colors)):
    newTurtle = RacingTurtle(i, colors[i])
    newTurtle.move_to_start()
    turtles.append(newTurtle)

# Race the turtles
over = False
while not over:
    moving = choice(turtles)
    over = moving.advance()
    if over:
        winning_color = moving.get_color()
        if bet_on == winning_color:
            print(f"The {winning_color} turtle won. You bet on {bet_on}. You win!")
        else:
            print(f"The {winning_color} turtle won. You bet on {bet_on}. You lose!")

screen.exitonclick()
