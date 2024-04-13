
from turtle import Turtle, Screen
from random import randint

colors = ["cornflowerblue", "coral", "purple", "crimson", "lightseagreen", "dimgray", "gold", "magenta"];
timmy = Turtle()
timmy.width(4)
timmy.pendown()

def draw_shape(sides):
  angle = 180 - ((sides - 2) * 180 / sides)
  color = colors[randint(0, len(colors) - 1)]
  print(f"sides: {sides}, angle: {angle}, color: {color}")
  timmy.color(color)
  for side in range(0, sides):
    timmy.forward(100)
    timmy.right(angle)

for sides in range(3, 13):
  draw_shape(sides)

my_screen = Screen()
my_screen.exitonclick()
