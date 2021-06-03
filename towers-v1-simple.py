#!/usr/bin/env python3

"""
towers-v1-simple.py
This program uses recursion to display a solution to the Towers of Hanoi
problem. See the accompanying README.md file for further information on
this project, the Towers of Hanoi problem, and our strategy for solving
it here.
"""

__author__ = 'Richard White, rwhite@crashwhite.com'
__version__ = '2017-07-18'

def move(height, source, intermediate, destination):
    """Determines the next move that should be made to move a disk."""
    if height == 1:      # if just one disk left, move it!
        print("move a disk from",source,"to",destination)
    else:
        # This is where the magic happens. If we haven't yet gotten
        # to a height of 1--if we're starting with 4 disks, say--
        # we'll first move the 3 disks to the intermediate location,
        # using destination as an intermediate. (Weird, right?)
        move(height - 1, source, destination, intermediate)
        # Once we've completed that, let's move the one remaining over:
        print("move a disk from",source,"to",destination)
        # Now move the remaining disks over using the source tower as
        # an intermediate!
        move(height - 1, intermediate, source, destination)

def main():
    print("Solving the 'Towers of Hanoi' problem")
    height = 10
    source = "A"
    intermediate = "B"
    destination = "C"
    move(height, source, intermediate, destination)
    print("Solution completed")

if __name__ == "__main__":
    main()



