
from turtle import Turtle, Screen
import random
import time
import math
import sys
from scoreboard import Scoreboard

SPEED = 1
NORTH = 90.0
SOUTH = 270.0
EAST = 0.0
WEST = 180.0
                  
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
        self.food.penup()
        valid_pos = False
        while not valid_pos:
            hpos = random.randint(-14, 14) * 20
            vpos = random.randint(-14, 14) * 20
            if not snake.is_snake_pos(hpos, vpos, False):
                valid_pos = True
        print(f"New food position: {hpos}, {vpos}")
        self.food.setx(hpos)
        self.food.sety(vpos)
        screen.update()

    def position(self):
        return self.food.position()
    
    def consume(self):
        self.food.reset()
        self.food.hideturtle()
    
class Snake:

    def __init__(self, start_length):
        self.currxcor = 0
        self.parts = []
        for i in range(0, start_length):
            part = SnakePart()
            part.get_turtle().setposition(self.currxcor, 0)
            self.currxcor -= 20
            self.parts.append(part)
        screen.update()
      
    def dump(self):
        for part in self.parts:
            print(f"Part: {part.get_turtle().position()}, color: {part.get_turtle().color()}")

    def length(self):
        return len(self.parts)
    
    def left(self):
        t = self.parts[0].get_turtle()
        print(f"Left, heading: {t.heading()}")
        # If snake is headed North or South, make it head West
        if t.heading() == NORTH or t.heading() == SOUTH:
            print("   Turning")
            t.setheading(WEST)
        
    def right(self):
        t = self.parts[0].get_turtle()
        print(f"Right, heading: {t.heading()}")
        # If snake is headed North or South, make it head East
        if t.heading() == NORTH or t.heading() == SOUTH:
            print("   Turning")
            t.setheading(EAST)

    def up(self):
        t = self.parts[0].get_turtle()
        print(f"Up, heading: {t.heading()}")
        # If snake is headed East or West, make it head North
        if t.heading() == EAST or t.heading() == WEST:
            print("   Turning")
            t.setheading(NORTH)

    def down(self):
        t = self.parts[0].get_turtle()
        print(f"Down, heading: {t.heading()}")
        # If snake is headed East or West, make it head South
        if t.heading() == EAST or t.heading() == WEST:
            print("   Turning")
            t.setheading(SOUTH)

    def move(self):
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
        return self.is_position_valid()

    def head_position(self):
        t_head = self.parts[0].get_turtle()
        return t_head.position()

    def add_segment(self):
        # Clone the last segment
        part = SnakePart(self.parts[len(self.parts) - 1])
        self.parts.append(part)
        
    def is_position_valid(self):
        valid = True
        head = self.parts[0].get_turtle()
        #print(f"coords: {head.position()}")
        if head.xcor() <= -300 or head.xcor() >= 300 or head.ycor() <= -300 or head.ycor() >= 300:
            #print("position invalid, out of range")
            valid = False
        else:
            print("checking whether snake looped back on itself")
            print(f"head position: {head.position()}")
            for i in range(1, len(self.parts)):
                pt = self.parts[i].get_turtle()
                #print(f"   part {i} position: {pt.position()}")
                #print(f"   head position: {head.position()}")
                if math.isclose(head.xcor(), pt.xcor(), abs_tol=0.003) and \
                        math.isclose(head.ycor(), pt.ycor(), abs_tol=0.003):
                    print("snake hit itself")
                    valid = False
                    break
        return valid

    def is_snake_pos(self, x, y, bCheckHeadOnly):
        retval = False
        for i in range(1, len(self.parts)):
            pt = self.parts[i].get_turtle()
            if math.isclose(x, pt.xcor(), abs_tol=0.003) and \
                    math.isclose(y, pt.ycor(), abs_tol=0.003):
                retval = True
                break
            if bCheckHeadOnly:
                break
        return retval
       
    def clear(self):
        for part in self.parts:
            t = part.get_turtle()
            t.reset()
            t.hideturtle()

def is_on_food():
    global food, snake
    head_pos = snake.head_position()
    food_pos = food.position()
    print(f"Snake head pos: {head_pos}, food pos: {food_pos}")
    return math.isclose(head_pos[0], food_pos[0], abs_tol=0.003) and \
        math.isclose(head_pos[1], food_pos[1], abs_tol=0.003)

def consume_food():
    global food, snake
    if is_on_food():
        print("Consuming food!")
        # Consume the existing food, add a snake segment, and make new food
        food.consume()
        snake.add_segment()
        # Update the scoreboard
        scoreboard.increment()
        food = Food()
    else:
        print("Not on food")

def init_snake():
    global snake
    if not snake is None:
        snake.clear()
    snake = Snake(3)

def init_food():
    global food
    if not food is None:
        food.consume()
    food = Food()

def move_til_done():
    global snake
    valid = snake.move()
    if valid:
        consume_food()
        screen.ontimer(move_til_done, 100)
    else:
        scoreboard.update_high_score()
        again = screen.textinput(title=f"Game Over!", prompt=f"Game over!\n\nPlay again? (Y/N)")
        if again is None:
            again = 'n'
        else:
            again.lower()
        if again == 'y':
            screen.listen()
            init_snake()
            init_food()
            scoreboard.reset()
            move_til_done()
        else:
            sys.exit()

def up():
    global snake
    snake.up()

def down():
    global snake
    snake.down()

def left():
    global snake
    snake.left()

def right():
    global snake
    snake.right()

def do_print():
    print("got key")

snake = None
food = None
init_snake()
init_food()
scoreboard = Scoreboard()

screen.onkey(key="Left", fun=left)
screen.onkey(key="Right", fun=right)
screen.onkey(key="Up", fun=up)
screen.onkey(key="Down", fun=down)
screen.onkey(key="p", fun=do_print)
screen.listen()

move_til_done()

screen.exitonclick()
