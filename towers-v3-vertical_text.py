#!/usr/bin/env python3

"""
towers-v3-vertical_text.py

This program uses recursion to display a solution to the Towers of Hanoi
problem. See the accompanying README.md file for further information on
this project, the Towers of Hanoi problem, and our strategy for solving
it here.

In this version, we'll display disk values on the screen in a vertical
orientation so that we have a crude graphical representation of the 
status of the towers as we go.
"""

__author__ = 'Richard White, rwhite@crashwhite.com'
__version__ = '2017-07-18'

from os import system
from time import sleep

def display():
    system("clear")
    print("\nMoves: ",move_count,"\n")
    """Displays the state of the global lists a, b, c as a series
    of vertical columns. Index i counts down from the maximum height
    (depth) of the columns; for any given column A, B, or C, if 
    index i has reached the height of the column (ie the length of 
    that columns list), we'll display that value.
    """
    for i in range(height - 1, -1, -1):
        # A
        if i < len(a):
            print("{0:^5}".format(a[i]),end='')
        else:
            print("{0:5}".format(""),end='')
        # B
        if i < len(b):
            print("{0:^5}".format(b[i]),end='')
        else:
            print("{0:5}".format(""),end='')
       # C
        if i < len(c):
            print("{0:^5}".format(c[i]),end='')
        else:
            print("{0:5}".format(""),end='')
        print()
    print(" ---  ---  ---")
    print("  A    B    C ")
    sleep(0.05)

def move(depth, source, intermediate, destination):
    global move_count
    """Determines the next move that should be made to move a disk."""
    if depth == 1:      # if just one disk left, move it!
        # print("move a disk from",source,"to",destination)
        destination.append(source.pop())
        move_count += 1
        display()
    else:
        # This is where the magic happens. If we haven't yet gotten
        # to a height of 1--if we're starting with 4 disks, say--
        # we'll first move the 3 disks to the intermediate location,
        # using destination as an intermediate. (Weird, right?)
        move(depth - 1, source, destination, intermediate)
        # Once we've completed that, let's move the one remaining over:
        # print("move a disk from",source,"to",destination)
        destination.append(source.pop())
        move_count += 1
        display()
        # Now move the remaining disks over using the source tower as
        # an intermediate!
        move(depth - 1, intermediate, source, destination)

def main():
    global a, b, c, height, move_count
    print("Solving the 'Towers of Hanoi' problem using lists to maintain")
    print("the state of the disks on the towers.")
    depth = 10
    height = depth
    move_count = 0
    # Initialize all three towers
    a = []
    for i in range(depth, 0, -1):
        a.append(i)
    b = []
    c = []
    display()
    move(depth, a, b, c)
    print("Solution completed")

if __name__ == "__main__":
    main()


