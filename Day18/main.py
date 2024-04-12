
from turtle import Turtle, Screen
import heroes

timmy = Turtle()
timmy.color("purple")
timmy.shape("turtle")

# square
for x in range(0, 4):
  timmy.forward(100)
  timmy.right(90)

# dashed line
timmy.penup()
timmy.left(180)
timmy.forward(20)
timmy.right(90)
for x in range(0, 10):
  timmy.pd()
  timmy.forward(20)
  timmy.pu()
  timmy.forward(20)

hero = heroes.gen()
print(hero) 





my_screen = Screen()
my_screen.exitonclick()
