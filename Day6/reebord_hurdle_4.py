def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_around():
    turn_left()
    turn_left()
    
def move_n(n):
    for x in range(0, n):
        move()
        
def draw_square(size):
    turn_left()
    move_n(size)
    turn_right()
    move_n(size)
    turn_right()
    move_n(size)
    turn_right()
    move_n(size)
    
def walk_until_wall_or_goal():
    while not wall_in_front() and not at_goal():
        move()
        
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()

while not at_goal():
    walk_until_wall_or_goal()
    if not at_goal():
        jump()




################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
