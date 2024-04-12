
from turtle import Turtle, Screen, colormode
from random import choice, randint
import colorgram

colors = colorgram.extract("Day18/source_painting.jpg", 12);
print(f"Colors: {colors}")
print(f"   0: {colors[0]}")
print(f"   0.rgb: {colors[0].rgb}")

WIDTH = 640
HEIGHT = 480
screen = Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)

timmy = Turtle()
timmy.penup()
timmy.speed("fastest")
colormode(255)

def random_color():
  return choice(colors).rgb

x = 5
y = 5
while y < 476:
  while x < 630:
    timmy.goto(x, y)
    timmy.dot(20, random_color())
    x += 30
  x = 5
  y += 30
        
screen.exitonclick()
