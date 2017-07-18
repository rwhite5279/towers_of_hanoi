#!/usr/bin/env python3

"""
towers.py
This program uses recursion to display a solution to the Towers of Hanoi
problem. See the accompanying README.md file for further information on
this project, the Towers of Hanoi problem, and our strategy for solving
it here.

In this version, we're returning to out lists to manage the tower, but 
each list (a, b, c) will be a list of Turtle objects, as opposed to 
integers. The turtles will be drawn onto the screen in an initial 
configuration, and then individually moved by the move command based on 
where they're being moved to. This requires some planning and calculation 
as outline in the README document.

Also, we've removed the display() function in this version, in favor of
manipulating the disks (turtles) directly, either in the main() function
or in the move function. Moving an individual turtle is much faster than
redwrawing all of them each time.

@author Richard White, rwhite@crashwhite.com
@version 2017-07-18
"""

from os import system
from time import sleep
import turtle

def move(depth, source, intermediate, destination):
    global height, move_count
    """Determines the next move that should be made to move a disk."""
    if depth == 1:      # if just one disk left, move it!
        turtle_to_move = source.pop()
        destination.append(turtle_to_move)
        # move that disk (turtle) from where it was to where it goes next
        # x = -400, b = 0, c = +400
        # y = - len(list) * 10
        if destination == a:
            x_coord = -400
        elif destination == b:
            x_coord = 0
        else:
            x_coord = 400
        turtle_to_move.goto(x_coord, -20 * (height - len(destination) + 1))
        move_count += 1
    else:
        # This is where the magic happens. If we haven't yet gotten
        # to a height of 1--if we're starting with 4 disks, say--
        # we'll first move the 3 disks to the intermediate location,
        # using destination as an intermediate. (Weird, right?)
        move(depth - 1, source, destination, intermediate)
        # Once we've completed that, let's move the one remaining over:
        turtle_to_move = source.pop()
        destination.append(turtle_to_move)
        # move that disk (turtle) from where it was to where it goes next
        if destination == a:
            x_coord = -400
        elif destination == b:
            x_coord = 0
        else:
            x_coord = 400
        turtle_to_move.goto(x_coord, -20 * (height - len(destination) + 1))
        move_count += 1
        # Now move the remaining disks over using the source tower as
        # an intermediate!
        move(depth - 1, intermediate, source, destination)

def main():
    global a, b, c, height, move_count
    print("Solving the 'Towers of Hanoi' problem using lists to maintain")
    print("the state of the disks on the towers.")
    depth = 7           # used to track depth of recursion
    height = depth      # used for height of graphical display
    move_count = 0      # tracks total number of disk moves for display
    turtle.setup(1100,800)
    win = turtle.Screen()
    # Initialize all three towers
    a = []
    for i in range(depth, 0, -1):
        # turtle will have a dimension based on scaled value
        # turtle 10 will have width of 10 * scale, etc.
        t = turtle.Turtle()
        t.shape("square")
        t.penup()
        t.speed(7)
        t.turtlesize(0.9, i, 0)     # 0.9 is the turtle height
        # Where do we "goto"?
        t.goto(-400, -i * 20)       # -i * 20 determines vertical position
        a.append(t)
    b = []
    c = []
    # Initial display of turtles (all at a)
    for i in range(height - 1, -1, -1):
        # A
        if i < len(a):
            a[i].showturtle()
    # Start recursively solving the problem!
    move(depth, a, b, c)
    print("Number of moves to complete:",move_count)
    win.exitonclick()               # Keeps the display from disappearing

if __name__ == "__main__":
    main()

