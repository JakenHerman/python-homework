'''
Created on Sep 30, 2015

@author: jakenherman
'''
import turtle
turtle.pensize(3)
turtle.speed('fastest')
turtle.hideturtle()

def circle(radius=50, cx=0, cy=0, color = 'black', fill= False):
    turtle.penup()
    turtle.goto(cx, cy - radius)
    turtle.pd()
    turtle.circle(radius)
    
def rectangle(length = 50, width = 30, x = 0, y = 0, color = 'black', fill = False):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(width)
    
    turtle.getscreen()._root.mainloop() #keep window open until close

circle()
rectangle(100, 80, 50, 50)