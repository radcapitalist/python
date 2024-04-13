
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    tim.left(22.5)

def turn_right():
    tim.right(22.4)

screen.listen()
screen.onkey(key="f", fun=move_forwards)
screen.onkey(key="b", fun=move_backwards)
screen.onkey(key="l", fun=turn_left)
screen.onkey(key="r", fun=turn_right)

screen.exitonclick()
