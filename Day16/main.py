
from turtle import Turtle, Screen
from prettytable import PrettyTable

# Turtle Graphics doc: https://docs.python.org/3/library/turtle.html

timmy = Turtle()

print(timmy)
timmy.shape("turtle")
timmy.color("coral")

timmy.forward(100)
timmy.left(45)
timmy.forward(90)
timmy.right(10)
timmy.backward(80)

my_screen = Screen()
print(my_screen.canvheight)

my_table = PrettyTable()
my_table.field_names = ["position", "number", "years of service"]
my_table.add_rows(
  [
    ["Deshaun Watson", "QB", 3],
    ["Nick Chubb", "RB", 5],
    ["David Njoku", "TE", 8],
  ]
)
my_table.align = "l"
print(my_table)

my_screen.exitonclick()


