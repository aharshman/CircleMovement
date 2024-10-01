# -*- coding: utf-8 -*-
"""
Alexander Harshman
12/7/2021
"""

# Importing all Classes
from graphics import *
from CircleButton import CButton
from random import randint
from math import sqrt


"""
Description: This function chooses and returns a random color

inputs:
    colorlist - The list of colors the face can be
    
Outputs:
    Color - The randomly selected color   
"""
def newcolor(colorlist):
    
    i = randint(0,3)
    color = colorlist[i]
    return color

"""
Description: My click function in my class wasn't working right so I had to 
improvise and I ended up using a distance function instead since I did not have
worry about the button being off.

inputs:
    p - The point where the user clicked
    x - The x coordinate where the center is
    y - The y coordinate where the center is
    
Outputs:
    Distance - The distance between the cetner of the face and the point
    the user clicked
"""

def distance(p, x, y): # p = the point where we clicked

    distance = sqrt((((x - p.getX())**2) + (y - p.getY())**2))
    
    return distance
    


def main():
    
# Making a window
    win = GraphWin('Smiley Face', 400, 400)
    win.setBackground('lightyellow')
    
#Setting Variables
    colorlist = ['green', 'lightgray', 'lightblue', 'pink']
    
    color = 'green'
    x, y = 200, 200
    b = CButton(win, Point(x, y), 25, ' ', color)
    
    eye1 = Point(x + 8, y - 8).draw(win)
    eye2 = Point(x - 8, y - 8).draw(win)
    mouth = Line(Point(x - 8, y + 8), Point(x + 8, y + 8)).draw(win)
    
    p = win.getMouse()
    b.activate()
    
# Making a infinite loop
    while True:

        d = distance(p, x, y)
        
    # The if statement tells whether or not the user clicked inside the circle
        if d > 25:
        
        # Getting x and y coords
            x = p.getX()
            y = p.getY()
            
        # Moving the previous button out of the way
            b.move(-1000, -1000)
            b = CButton(win, Point(x, y), 25, ' ', color)
            
        # Removing the face
            eye1.undraw()
            eye2.undraw()
            mouth.undraw()
             
        # Moving the face
            eye1 = Point(x + 8, y - 8).draw(win)
            eye2 = Point(x - 8, y - 8).draw(win)
            mouth = Line(Point(x - 8, y + 8), Point(x + 8, y + 8)).draw(win)
            
            p = win.getMouse()
            
        else:
            
        # Getting a new color
            color = newcolor(colorlist)
            
        # Making a new button
            bnew = CButton(win, Point(x, y), 25, ' ', color)
            
        # Making a new face
            neweye1 = Point(x + 8, y - 8).draw(win)
            neweye2 = Point(x - 8, y - 8).draw(win)
            newmouth = Line(Point(x - 8, y + 8), Point(x + 8, y + 8)).draw(win)
            
        # Removing old face
            eye1.undraw()
            eye2.undraw()
            mouth.undraw()
            
            p = win.getMouse()
            
        # Moving the previous button out of the way
            b.move(-1000, -1000)
            
        # Resetting variables
            b = bnew
            eye1 = neweye1
            eye2 = neweye2
            mouth = newmouth
            
    win.getMouse()
    win.close()

main()