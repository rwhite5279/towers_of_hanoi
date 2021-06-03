#!/usr/bin/env python3

"""
towers-v4-object-vertical_text.py
This program uses recursion to display a solution to the Towers of Hanoi
problem. See the accompanying README.md file for further information on
this project, the Towers of Hanoi problem, and our strategy for solving
it here.

In this version, we'll use Tower objects (instead of a list) to represent
the disks on each vertical tower. The appearance of the towers produced 
in the display, however, is exactly the same as the previous version.
"""

__author__ = 'Richard White, rwhite@crashwhite.com'
__version__ = '2017-07-18'

from os import system
from time import sleep

class Tower():
    """This class represents a tower with a given number of disks on it.
    """
    def __init__(self, name):
        self.name = name
        self.disks = []

    def asList(self):
        return self.disks

    def getHeight(self):
        return len(self.disks)

    def getDisk(self, item):
        """Assumes that i is a valid disk index!"""
        return self.disks[item]

    def getName(self):
        return self.name

    def addDisk(self,value):
        self.disks.append(value)

    def popDisk(self):
        return self.disks.pop()

    def moveFrom(self, other):
        self.disks.append(other.popDisk())

    
def display():
    system("clear")
    print("\nMoves: ",move_count,"\n")
    """Displays the state of the global lists a, b, c."""
    for i in range(height - 1, -1, -1):
        # A
        if i < a.getHeight():
            print("{0:^5}".format(a.getDisk(i)),end='')
        else:
            print("{0:5}".format(""),end='')
        # B
        if i < b.getHeight():
            print("{0:^5}".format(b.getDisk(i)),end='')
        else:
            print("{0:5}".format(""),end='')
       # C
        if i < c.getHeight():
            print("{0:^5}".format(c.getDisk(i)),end='')
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
        destination.addDisk(source.popDisk())
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
        destination.addDisk(source.popDisk())
        move_count += 1
        display()
        # Now move the remaining disks over using the source tower as
        # an intermediate!
        move(depth - 1, intermediate, source, destination)

def main():
    global a, b, c, height, move_count
    print("Solving the 'Towers of Hanoi' problem using a Tower class to ")
    print("maintain the state of the disks on the towers.")
    depth = 10
    height = depth
    move_count = 0
    # Initialize all three towers
    a = Tower("A")
    for i in range(depth, 0, -1):
        a.addDisk(i)
    b = Tower("B")
    c = Tower("C")
    display()
    move(depth, a, b, c)
    print("Solution completed")

if __name__ == "__main__":
    main()


