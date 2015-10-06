import turtle

userSides = input("how many sides? ")

turtle.circle(50, extent=None, steps=int(userSides))

def interiorAngleOfPolygon(sides):
    angle = 360 / int(sides)
    print(angle)
    return angle

turtle.penup()
turtle.goto(0, -50)
turtle.write('the interior angles are ' + str(round(interiorAngleOfPolygon(userSides), 2))
                                                                 + ' degrees')
