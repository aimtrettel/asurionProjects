import math

# Define a class called Apple with four instance variables that represent four
# attributes of an apple.
class Apple():
    def __init__(self, c, f, h, w):
        self.color = c
        self.flavor = f
        self.heavy = h
        self.worm = w
        
a = Apple("red", "sweet", 12.3, False)
print(a.color)
print(a.flavor)
print(a.heavy)
print(a.worm)

print("---------------------------------------")
# Create a Circle class with a method called area that calculates and returns
# its area. Then create a Circle object, call area on it, and print the result.
# Use Python's pi function in the built-in math module.
class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi * (self.radius**2)

c = Circle(3.5)
print(c.area()) #should be 38.48

print("---------------------------------------")
# Create a Triangle class with a method called area that calculates and returns
# its area. Then create a Triangle object, call area on it, and print the
# result.
class Triangle():
    def __init__(self, h, b):
        self.height = h
        self.base = b

    def area(self):
        return (self.height * self.base) / 2
    
t = Triangle(4, 5)
print(t.area()) #should be 10

print("---------------------------------------")
# Make a Hexagon class with a method called calculate_perimeter that calculates
# and returns its perimeter. Then create a Hexagon object, call
# calculate_perimeter on it, and print the result.
class Hexagon():
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return 6 * self.side

h = Hexagon(1)
print(h.calculate_perimeter()) #should be 6
