# Create Rectangle and Square classes with a method called calculate_perimeter
# that calculates the perimeter of the shapes they represent. Create Rectangle
# and Square objects and call the method on both of them.
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def calculate_perimeter(self):
        return (self.length * 2) + (self.width * 2)

class Square():
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return (self.side * 4)


rect = Rectangle(2, 3)
sq = Square(2)
print(rect.calculate_perimeter())
print(sq.calculate_perimeter())

print("--------------------------------------------")
# Define a method in your Square class called change_size that allows you to
# pass in a number that increases or decreases (if the number is negative) each
# side of a Square object by that number.
class Square2():
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return (self.side * 4)

    def change_size(self, num):
        self.side += num


sq2 = Square2(2)
print(sq2.calculate_perimeter())
sq2.change_size(-1)
print(sq2.calculate_perimeter())
sq2.change_size(3)
print(sq2.calculate_perimeter())

print("--------------------------------------------")
# Create a class called Shape. Define a method in it called what_am_i that
# prints "I am a shape" when called. Change your Square and Rectangle classes
# from the previous challenges to inherit from Shape, create Square and
# Rectangle objects, and call the new method on both of them.
class Shape():
    def what_am_i(self):
        print("I am a shape")

class Rectangle3(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def calculate_perimeter(self):
        return (self.length * 2) + (self.width * 2)

class Square3(Shape):
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return (self.side * 4)

    def change_size(self, num):
        self.side += num


rect3 = Rectangle3(2, 3)
sq3 = Square3(2)
rect3.what_am_i()
sq3.what_am_i()

print("--------------------------------------------")
# Create a class called Horse and a class called Rider. Use composition to
# model a horse that has a rider.
class Horse():
    def __init__(self, n, b, h, r):
        self.name = n
        self.breed = b
        self.height = h
        self.rider = r

class Rider():
    def __init__(self, n, h):
        self.name = n
        self.height = h


jack = Rider("Jack Sparrow", 6)
shadow = Horse("Shadow", "Pinto", 8, jack)
print(shadow.rider.name)
