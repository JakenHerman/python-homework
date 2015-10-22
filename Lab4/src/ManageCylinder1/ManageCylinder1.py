'''
Created on Oct 21, 2015

@author: jakenherman
'''
from CylinderModule1 import *

def main():
    
    bottle = Cylinder1()
    
    bottle.radius = 4
    bottle.height = 8
    
    print("The radius and height of the bottle are: ", bottle.radius, "and ", bottle.height)
    print("The perimeter of the bottle end circle is ", bottle.getPerimeter())
    print("The end circle area of the bottle is", bottle.getEndArea())
    print("The side are of the bottle is", bottle.getSideArea())
    print("The total surface of the bottle is ", bottle.getSurfaceArea())
    print("The volume of the bottle is ", bottle.getVolume())
    
main()