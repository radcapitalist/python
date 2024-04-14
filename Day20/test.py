
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

class SnakePart:
    turtle = Turtle()
    turtle.shape('square')
    turtle.color('white')
    turtle.penup()

    def get_turtle(self):
        return self.turtle

parts = []

turtle = Turtle()
turtle.shape("square")
turtle.color("red")
turtle.penup()
turtle.setposition(0, 0)

turtle = Turtle()
turtle.shape("square")
turtle.color("blue")
turtle.penup()
turtle.setposition(-20, 0)

turtle = Turtle()
turtle.shape("square")
turtle.color("green")
turtle.penup()
turtle.setposition(-40, 0)


screen.exitonclick()