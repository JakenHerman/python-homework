'''
Created on Sep. 30, 2015
Assignment 2: MyDrawing
@author: Jaken C. Herman
@email: jch053@shsu.edu
'''

import turtle
from Graphics2D.GraphicsAndPatternLibrary import *
from Graphics2D import GraphicsAndPatternLibrary

myTurtle = turtle.Turtle()

myTurtle.pensize(3)
myTurtle.circle()

def main():
    GraphicsAndPatternLibrary.circle(50, -100, 0, 'blue', True)
    GraphicsAndPatternLibrary.chessboard(-40, 10, 80)
    GraphicsAndPatternLibrary.rectangle(50, 30, 60, 70,'green', True)
    GraphicsAndPatternLibrary.polygon(50, 50, 90, 150, 6, 'red', True)

    return

main()    #  This is the statement to call main()