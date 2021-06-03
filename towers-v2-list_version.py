#!/usr/bin/env python3

"""
towers-v2-list_version.py

This program uses recursion to display a solution to the Towers of Hanoi
problem. See the accompanying README.md file for further information on
this project, the Towers of Hanoi problem, and our strategy for solving
it here.

In this version, we'll display disk values on the screen so that we have
a crude graphical representation of the status of the towers as we go.
"""

__author__ = 'Richard White, rwhite@crashwhite.com'
__version__ = '2017-07-18'

from os import system
from time import sleep

def display():
    system("clear")
    """Displays the state of the global lists a, b, c."""
    print("A | ",a)
    print("B | ",b)
    print("C | ",c)
    print()
    # sleep(0.01)   # Uncomment this to slow down the display

def move(depth, source, intermediate, destination):
    """Determines the next move that should be made to move a disk."""
    if depth == 1:      # if just one disk left, move it!
        # print("move a disk from",source,"to",destination)
        destination.append(source.pop())
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
        display()
        # Now move the remaining disks over using the source tower as
        # an intermediate!
        move(depth - 1, intermediate, source, destination)


def main():
    print("Solving the 'Towers of Hanoi' problem using lists to maintain")
    print("the state of the disks on the towers.")
    height = 10
    # Initialize all three towers
    global a, b, c
    a = []
    for i in range(height, 0, -1):
        a.append(i)
    b = []
    c = []
    display()
    move(height, a, b, c) 
    print("Solution completed")

if __name__ == "__main__":
    main()

