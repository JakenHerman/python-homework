import turtle

turtle.speed(3)
turtle.hideturtle()
turtle.pensize(3)
user_radius = input("Input Radius: ")

#initial ring
turtle.pu()
turtle.goto(0, -user_radius)
turtle.pd()
turtle.circle(user_radius)
turtle.pu()
turtle.lt(90)
turtle.fd(user_radius)
black_coord = turtle.pos()
turtle.write(black_coord , align='center')
turtle.rt(180)
turtle.fd(user_radius)
turtle.lt(90)

#blue ring
turtle.pu()
turtle.lt(180)
turtle.fd((user_radius*1.25) + 1)
turtle.rt(90)
turtle.fd(user_radius)
turtle.color('blue')
turtle.pd()
turtle.circle(user_radius)
turtle.pu()
turtle.lt(90)
turtle.fd(user_radius)
blue_coord = turtle.pos()
turtle.color('black') #for text
turtle.write(blue_coord, align='center')
turtle.rt(180)
turtle.fd(user_radius)

#yellow ring
turtle.rt(135)
turtle.fd(user_radius/1.25)
turtle.color('yellow')
turtle.pd()
turtle.circle(user_radius)
turtle.pu()
turtle.left(90)
turtle.fd(user_radius)
yellow_coord = turtle.pos()
turtle.color('black') #for text
turtle.write(yellow_coord, align='center')
turtle.right(180)
turtle.fd(user_radius)

#red ring
turtle.rt(135)
turtle.pu()
turtle.goto(0, -user_radius)
turtle.fd((user_radius*3.25) + 1)
turtle.lt(90)
turtle.fd(user_radius)
turtle.color('red')
turtle.pd()
turtle.circle(user_radius)
turtle.pu()
turtle.color('black')
turtle.lt(90)
turtle.fd(user_radius)
red_coord = turtle.pos()
turtle.write(red_coord, align='center')

#green ring
turtle.rt(180)
turtle.goto(yellow_coord)
test = turtle.pos()[0] #get yellow_coord x position
turtle.fd(-(2 * test)) #double yellow_coord x position. negative because we want absolute value. could alternatively use abs()
turtle.rt(90)
turtle.fd(user_radius)
turtle.lt(90)
turtle.color('green')
turtle.pd()
turtle.circle(user_radius)
turtle.pu()
turtle.left(90)
turtle.fd(user_radius)
green_coord = turtle.pos()
turtle.color('black')
turtle.write(green_coord, align='center')


turtle.getscreen()._root.mainloop() #keep window open until close
