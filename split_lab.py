statement1 = "canvas1.create_rectangle(10, 10, 190, 90, tags='rect')"
statement2 = "canvas2.create_square(15, 55, 125, 160, tags='sqr')"
statement3 = "canvas3.create_polygon(20, 13, 175, 79, tags='plygn')"
statement4 = "canvas4.create_oval(18, 25, 110, 85, tags='rect')"

#example statement
#canvas1.create_rectangle(10,10,190,90,tags='rect')
#object = canvas1
#shape = rectangle
#boudary position: xstart=10; ystart=10; xEnd=190; yEnd=90;
#tag name = rect
#number of vowels = 10

#
#''' Statement 1 '''
#

object_1_name_split = statement1.split(".")
object_1_name = object_1_name_split[:-1]

shape_1_name = statement1.split("create_", 2)
shape_1_shave = shape_1_name[1].split("(")
print(shape_1_shave[0])

#
#''' Statement 2 '''
#

object_2_name_split = statement2.split(".")
object_2_name = object_2_name_split[:-1]

shape_2_name = statement2.split("create_", 2)
shape_2_shave = shape_2_name[1].split("(")
print(shape_2_shave[0])


print(object_1_name[0])
print(object_2_name[0])
