'''
Created on Sep 30, 2015
Assignment 2: MyDrawing
@author: Jaken C. Herman
@email: jch053@shsu.edu
'''
import turtle

def circle(radius = 50, cx = 0, cy = 0, color = 'black', fill = False):
    turtle.penup()
    if fill == True:
    
        turtle.goto(cx, cy - radius)
        turtle.color(color)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(radius)
        turtle.end_fill()
        turtle.penup()
    else:
        turtle.penup()
        turtle.goto(cx, cy - radius)
        turtle.pd()
        turtle.circle(radius)
        turtle.penup()
    return
    
def rectangle(length = 50, width = 30, x = 0, y = 0, color = 'black', fill = False):
    turtle.pensize(3)
    turtle.speed('fastest')
    turtle.hideturtle()
    if fill == True:
        turtle.color(color)
        for i in range(width): 
            turtle.setposition(x, (y+i))
            turtle.pendown()
            turtle.setposition((x+length), (y+i))
            turtle.penup()
    else:
        turtle.penup()
        turtle.goto(x,y)
        turtle.color(color)
        turtle.pendown()
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.penup()

    return
    
def polygon(side = 50, angle = None, xstart = None, ystart = None, numberSides = 3, color = 'black', fill = False):
    turtle.pensize(3)
    turtle.speed('fastest')
    turtle.hideturtle()
    if angle != None:
        turtle.left(angle)
    
    turtle.penup()
    if fill == True:
        if xstart != None or ystart != None:
            turtle.goto(xstart, ystart)
        else:
            turtle.goto(0, 0)
        turtle.color(color)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(side, 360, numberSides)
        turtle.end_fill()
        turtle.penup()
        
    else:
        turtle.goto(xstart, ystart)
        turtle.color(color)
        turtle.pendown()
        turtle.circle(side, 360, numberSides)
        turtle.penup()
    
    return

def chessboard(xstart = None, ystart = None, side = 40, color = 'black', background = 'white'):
    turtle.pensize(3)
    turtle.speed('fastest')
    turtle.hideturtle()
    
    turtle.setposition(xstart, ystart)
    turtle.pendown()
    turtle.color(background)
    turtle.fill(True)
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)
    turtle.fill(False)
    turtle.color(color)
    turtle.fill(False)
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)
    turtle.fill(False)
    turtle.penup()  
    for k in range(4):
        if k == 0 or k == 2:
            turtle.setposition(xstart, (ystart + (k * (side / 4))))
            for i in range(4):
                if i % 2 == 0:
                    draw_filled_square((side / 4), (side/4))
                else:
                    draw_unfilled_square((side / 4), (side / 4))
                turtle.forward((side / 4))
            turtle.penup()
        elif k == 1:
            turtle.setposition(xstart, (ystart + side / 4))
            for j in range(4):
                if j % 2 == 0:
                    draw_unfilled_square((side / 4), (side / 4))
                else:
                    draw_filled_square((side / 4), (side / 4))
                turtle.forward((side / 4))
            turtle.penup()
        else:
            turtle.setposition(xstart, (ystart + (k * (side / 4))))
            for j in range(4):
                if j % 2 == 0:
                    draw_unfilled_square((side / 4), (side / 4))
                else:
                    draw_filled_square((side / 4), (side / 4))
                turtle.forward((side / 4))
        turtle.penup()      
    k += (side / 4)
    return

def rhombus(side = 50, xstart = None, ystart = None, color='black', fill = False):
    turtle.pensize(3)
    turtle.speed('fastest')
    turtle.hideturtle()
    if fill == True:
        polygon(side, None, xstart, ystart, 3, color, True)
        turtle.right(180)
        polygon(side, None, xstart, ystart, 3, color, True)
    else:
        polygon(side, None, xstart, ystart, 3, color, False)
        turtle.right(180)
        polygon(side, None, xstart, ystart, 3, color, False)
    
    return
 


'''
BELOW ARE ADDED FUNCTIONS I CREATED IN ORDER TO MAKE A NICE CHESSBOARD FUNCTION
'''

def draw_filled_square(size, loop_range):    
    """Draw a square by drawing a line and turning through 90 degrees 4 times"""
    turtle.pendown()
    turtle.fill(True)
    for _ in range(loop_range):
        turtle.forward(size)
        turtle.left(90)
    turtle.fill(False)
    turtle.penup()
    
def draw_unfilled_square(size, loop_range):    
    """Draw a square by drawing a line and turning through 90 degrees 4 times"""
    turtle.pendown()
    turtle.fill(False)
    for _ in range(loop_range):
        turtle.forward(size)
        turtle.left(90)
    turtle.fill(False)
    turtle.penup()   
    

turtle.getscreen()._root.mainloop() #keep window open until close