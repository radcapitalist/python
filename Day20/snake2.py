
from turtle import Turtle, Screen
import random
import time

SPEED = 10

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

class SnakePart:
    count = 0
    def __init__(self, clone_from = None):
        if clone_from is None:
            self.turtle = Turtle()
            self.turtle.speed(SPEED)
            self.turtle.shape('square')
            self.turtle.color("white")
            SnakePart.count += 1
            self.turtle.penup()
        else:
            self.turtle = clone_from.get_turtle().clone()

    def get_turtle(self):
        return self.turtle
    
    def dump(self, name):
        return f"{name}:  pos {self.turtle.position()}  heading {self.turtle.heading()}"


class Food:
    def __init__(self):
        self.food = Turtle()
        self.food.shape("circle")
        self.food.color("blue")

class Snake:
    parts = []

    def __init__(self, start_length):
        currxcor = 0
        for i in range(0, start_length):
            part = SnakePart()
            part.get_turtle().setposition(currxcor, 0)
            currxcor -= 20
            self.parts.append(part)
        screen.update()
      
    def dump(self):
        for part in self.parts:
            print(f"Part: {part.get_turtle().position()}, color: {part.get_turtle().color()}")

    def left(self):
        print("\nTurning Left\n")
        t = self.parts[0].get_turtle()
        t.setheading((t.heading() + 90) % 360)
        
    def right(self):
        print("\nTurning Right\n")
        t = self.parts[0].get_turtle()
        t.setheading((t.heading() - 90 + 360) % 360)

    def move(self):
        print("\nMove\n")
        for i in range(len(self.parts) - 1, -1, -1):
            part = self.parts[i]
            t = part.get_turtle()
            if i == 0:
                t.forward(20)
            else:
                tNext = self.parts[i - 1].get_turtle()
                t.setx(tNext.xcor())
                t.sety(tNext.ycor())
        screen.update()


    def add_segment(self):
        # Clone the last segment
        part = SnakePart(self.parts[len(self.parts) - 1])
        self.parts.append(part)
        

snake = Snake(3)

# snake.move()
# snake.move()
# snake.move()
# snake.right()
# snake.move()
# snake.move()
# snake.move()
# snake.move()

screen.listen()
screen.onkey(key="l", fun=snake.left)
screen.onkey(key="r", fun=snake.right)
screen.onkey(key="m", fun=snake.move)
screen.onkey(key="a", fun=snake.add_segment)

screen.exitonclick()