
from turtle import Turtle, Screen, colormode
import heroes
from random import choice, randint

angles = [0, 90, 180, -90]
distance = 30
timmy = Turtle()
timmy.width(10)
timmy.pendown()
timmy.hideturtle()
timmy.speed("fastest")
colormode(255)

def random_color():
   r = randint(0, 255)
   g = randint(0, 255)
   b = randint(0, 255)
   return (r, g, b)

def set_color():
    color = random_color()
    timmy.pencolor(color)
  
def random_turn():
   timmy.right(choice(angles))

def random_step():
   random_turn()
   set_color()
   timmy.forward(distance)

for _ in range(0, 1000):
   random_step()

my_screen = Screen()
my_screen.exitonclick()
