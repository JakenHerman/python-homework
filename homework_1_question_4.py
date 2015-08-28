import turtle

#pen-preparation
turtle.pensize(2)
turtle.penup()

#bottom-most-line
turtle.goto(-100, -25)
turtle.pendown()
turtle.goto(25, -25)
turtle.penup()

#top-of-face-rectangle
turtle.goto(-100, 25)
turtle.pendown()
turtle.goto(25, 25)
turtle.penup()

#left-side-of-face-rectangle
turtle.goto(-100, 25)
turtle.pendown()
turtle.goto(-100, -25)
turtle.penup()

#right-side-of-face-rectangle
turtle.goto(25, 25)
turtle.pendown()
turtle.goto(25, -25)
turtle.penup()

#left-side-top-rectangle
turtle.goto(-100, 25)
turtle.pendown()
turtle.left(45)
turtle.goto(-60, 50)
turtle.penup()

#topmost-line
turtle.right(45)
turtle.pendown()
turtle.goto(65, 50)
turtle.penup()

#rightmost-line-face-rectangle
turtle.right(135)
turtle.pendown()
turtle.goto(25, 25)
turtle.penup()
turtle.goto(65, 50)

#right-top-line
turtle.left(135)
turtle.right(90)
turtle.pendown()
turtle.goto(65, 5)
turtle.penup()
turtle.right(135-90)

#right-bottom-line
turtle.pendown()
turtle.goto(25, -25)
turtle.penup()
turtle.left(135+90)
turtle.right(45)
turtle.goto(65, 5)
turtle.left(135)

#midline
turtle.pendown()
turtle.goto(-60, 5)

#back-left-line
turtle.goto(-60, 50)
turtle.penup()
turtle.goto(-60, 5)

#last-line
turtle.pendown()
turtle.goto(-100, -25)
turtle.penup()

