from karel.stanfordkarel import *

"""
File: SteepleChaseKarel.py
--------------------------
Karel runs a steeple chase the is 9 avenues long.
Hurdles are of arbitrary height and placement.
"""

"""
To run a race that is 9 avenues long, we need to move
forward or jump hurdles 8 times.
"""

def turn_right():
    for i in range(3):
        turn_left()


def descend_hurdle():
    turn_right()
    while front_is_clear():
        move()
    turn_left()

def ascend_hurdle():
    turn_left()
    while right_is_blocked():
        move()


def main():
    for i in range(9):
        if front_is_clear():
            move()
        else:
            ascend_hurdle()
            turn_right()
            move()
            descend_hurdle()
# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
