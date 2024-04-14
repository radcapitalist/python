
from turtle import Turtle, Screen
import random

SPEED = 10

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

class SnakePart:
    def __init__(self, clone_from = None):
        if clone_from is None:
            self.turtle = Turtle()
            self.turtle.speed(SPEED)
            self.turtle.shape('square')
            self.turtle.color('white')
            self.turtle.penup()
        else:
            self.turtle = clone_from.get_turtle().clone()

    def get_turtle(self):
        return self.turtle
    
    def dump(self, name):
        print(f"{name}:  pos {self.turtle.position()}  heading {self.turtle.heading()}")


class Food:
    def __init__(self):
        self.food = Turtle()
        self.food.shape("")
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
      
    def dump(self):
        for part in self.parts:
            print(f"Part: {part.get_turtle().position()}, color: {part.get_turtle().color()}")

    def left(self):
        t = self.parts[0].get_turtle()
        t.setheading((t.heading() + 90) % 360)
        # turn should include 2 moves to keep the tail part from being adjacent to the head portion
        self.move()
        self.move()
        
    def right(self):
        t = self.parts[0].get_turtle()
        t.setheading((t.heading() - 90 + 360) % 360)
        # turn should include a move so we don't get two turns before a move
        self.move()
        self.move()

    def move(self):
        print("\nMove\n")
        for i in range(0, len(self.parts)):
            self.parts[i].dump(str(i))
            t = self.parts[i].get_turtle()
            if i > 0:
                self.parts[i - 1].dump(str(i - 1))
                t_prev = self.parts[i-1].get_turtle()
                # Has the segment in front of me turned?
                if not t.heading() == t_prev.heading():
                    # Yes, it has turned. If I'm caught up to him on the relevant axis, it's time for me to turn
                    # North = 90, South = 270, East = 0, West = 180
                    if t_prev.heading() == 90 or t_prev.heading() == 270:
                        # Segment in front is heading north or south, so check x for caught up
                        if t.xcor() == t_prev.xcor():
                            print(f"{i} is turning")
                            t.setheading(t_prev.heading())
                        else:
                            print(f"{i} needs to catch up")
                    else:
                        # Segment in front is heading east or west, so check y for caught up
                        if t.ycor() == t_prev.ycor():
                            print(f"{i} is turning")
                            t.setheading(t_prev.heading())
                        else:
                            print(f"{i} needs to catch up")
            t.forward(20)
        

    def add_segment(self):
        # Clone the last segment
        part = SnakePart(self.parts[len(self.parts) - 1])
        self.parts.append(part)
        # Move the new segment next to the one we cloned it from
        t = part.get_turtle()
        if t.heading() == 0: # East
            t.setx(t.xcor() - 20)
        elif t.heading() == 90: # North
            t.sety(t.ycor() - 20)
        elif t.heading() == 180: # West
            t.setx(t.xcor() + 20)
        elif t.heading() == 270: # North
            t.sety(t.ycor() - 20)

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