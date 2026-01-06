#W8A1: 
pi = 3.14
class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    
    def total_area(self):
        return 2*pi*self.radius*self.height + 2*pi*self.radius**2
    def volume(self):
        return pi*self.radius**2*self.height

r = int(input()))
h = int(input())
t = Cylinder(r,h)
print (f"Total Area: {t.total_area():.2f}")
print (f"Volume: {t.volume():.2f}")

#W8A2: 
