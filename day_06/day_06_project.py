""" This is just copy from the Reeborg code, the errors
displayed are due to many functions called without
having them defined """


def turn_right():
    """This function makes the robot turn itself until it faces right"""
    turn_left()
    turn_left()
    turn_left()


# Loop that helps the robot reach the goal    
while not at_goal():
    if right_is_clear(): # if the right is clear
        turn_right()
        move()
    elif front_is_clear(): # if there is nothing in the front
        move()
    else:
        turn_left()