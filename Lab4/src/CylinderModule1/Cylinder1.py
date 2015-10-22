import math

class Cylinder1:
    def __init__(self, radius, height):
        self.radius = 1
        self.height = 1
    
        self.r = float(self.radius)
        self.h = float(self.height)
    
    def Cylinder1(self, r, h):
        return
    
    def getPerimeter(self, r):
        return (2*math.pi*r)
    
    def getEndArea(self, r):
        return (2*math.pi*r** 2)
    
    def SideArea(self, h):
        return (2*math.pi*h)
    
    def SurfaceArea(self, r, h):
        return(self.getEndArea(self, r) + self.getSideArea(self, h))
    
    def getVolume(self, r, h):
        return( 2*math.pi*r*h)
    
        
        
        