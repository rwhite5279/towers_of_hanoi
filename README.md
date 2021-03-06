PROJECT: Towers of Hanoi
========================

This project describes a text-based, graphical-text, and graphical
solution to the Towers of Hanoi problem using Python3.

@author Richard White, rwhite@crashwhite.com
@version 2017-07-18

Introduction
------------

This project is designed to explore the use of recursion in Python, 
specifically via the Towers of Hanoi problem. Additionally, this
project will examine ways in which graphical displays can be used to
enhance the understanding of a problem/solution. *Additionally*, the
progress of the development of this project for students will be 
managed using `git`, so that students have an example of the software
development process over time.

Contents of this Project
------------------------

The `towers_of_hanoi` direction includes:

* `README.md`  
    this file
* `towers-v1-simple.py`  
    This is a text-based solution to the Towers of Hanoi problem.
* `towers-v2-list_based.py`  
    This is a list-based solution in which three lists are used to keep 
    track of the state of each tower. These lists are then printed out 
    after every mode of a disk, allowing us to view a simple representation 
    of the status of each tower.
* `towers-v3-vertical_text.py`  
    This is the same algorithmic solution as v2 above (using lists), but
    the display() method has been modified to present the results
    vertically, a more intuitive format that matches with the physical
    process of moving disks. This version is an important step toward
    working toward a purely graphics-based representation of the solution.
* `towers-v4-object-vertical_text.py`  
    This solution offers the same algorithm, but with a Tower class used
    to manage the list of disks. The advantage of writing a Tower class is
    that the lisk manipulation is hidden from the user. The disadvantage is
    that, for programmers comfortable with lists, the class is another
    layer of abstraction. This is still just a vertical column of values
    used to represent the towers. We need to move on to the graphics!
* `towers-v5-list-turtle_based.py`
    This solution is truly graphical based, with each disk on the tower
    represented by a rectangle of proportional width, implemented as a "turtle"
    using Python's turtle graphics. One of the major challenges in this version
    is getting the appropriate disk (turtle) to display at an appropriate 
    position on the screen. Miscellaneous pixel adjustments are present 
    throughout this version. One of the nice things about this system is the
    fact that the screen doesn't need to be redrawn for each disk move: a disk
    can be moved more-or-less directly to its new position on an adjacent tower.
    Although the current version is just a tower of 6 and with a turtle speed of 2,
    those values can be adjusted in the program. Set the turtle speed to 0 to have
    it proceed as quickly as possible!


The Towers of Hanoi Problem
---------------------------

From Miller & Ranum: "The Tower of Hanoi puzzle was invented by the 
French mathematician Edouard Lucas in 1883. He was inspired by a 
legend that tells of a Hindu temple where the puzzle was presented 
to young priests. At the beginning of time, the priests were given 
three poles and a stack of 64 gold disks, each disk a little smaller 
than the one beneath it. Their assignment was to transfer all 64 disks 
from one of the three poles to another, with two important constraints. 
They could only move one disk at a time, and they could never place a 
larger disk on top of a smaller one. The priests worked very efficiently, 
day and night, moving one disk every second. When they finished their 
work, the legend said, the temple would crumble into dust and the world 
would vanish."

Algorithmic Solution
--------------------

The solution to the Towers of Hanoi problem is one that can be arrived
at relatively quickly using the concept of recursion (making it ideal as
a context for introductory Computer Science students!).

We begin with three tower locations A, B, and C, and a series of three
disks on tower A:

          [_1_]
        [___2___]
     [______3______] 
    =================     ================     =================
        Tower A                Tower B              Tower C

Our "Source" tower is A, our "Destination" tower is C, and our 
"Intermediate" tower is B. If we can get all of the disks but the last one 
to our intermediate tower... 

                                [_1_]
     [______3______]          [___2___]  
    =================     ================     =================
        Tower A                Tower B              Tower C

... we can move the last disk from Tower A to Tower C, and then move the 
remaining disks back over from the intermediate to the destination:

                                [_1_]
                              [___2___]          [______3______] 
    =================     ================     =================
        Tower A                Tower B              Tower C


How to Use this Software
------------------------

To run `towers.py`:

1. in a terminal, navigate to the `towers_of_hanoi` directory:

        $ cd path/to/towers_of_hanoi

2. use Python3 to run the desired program:

        $ python3 towers-v2-list_based.py

The program will display a solution to the Towers of Hanoi problem for a
given number of disks.


