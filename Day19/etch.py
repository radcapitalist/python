
from turtle import Turtle, Screen

tim = Turtle()
startpos = tim.position()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    tim.setheading(tim.heading() - 5)

def turn_right():
    tim.setheading(tim.heading() + 5)

def reset():
    tim.goto(startpos[0], startpos[1])
    tim.setheading(0)
    tim.clear()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_right)
screen.onkey(key="d", fun=turn_left)
screen.onkey(key="c", fun=reset)

screen.exitonclick()
