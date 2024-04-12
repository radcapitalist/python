
from turtle import Turtle, Screen, colormode
import heroes
from random import choice, randint

angles = [0, 90, 180, -90]
radius = 100
timmy = Turtle()
timmy.width(2)
timmy.pendown()
#timmy.hideturtle()
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
  
def draw_circle():
    timmy.circle(radius)

for _ in range(0, 180):
  set_color()
  draw_circle()
  timmy.right(2)

my_screen = Screen()
my_screen.exitonclick()
