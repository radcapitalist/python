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
    
def walk_until_wall():
    while not wall_in_front():
        move()
        
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in range(0, 6):
    walk_until_wall()
    jump()




################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
