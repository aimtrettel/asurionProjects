# Add a square_list class variable to a class called Square so that every time
# you create a new Square object, the new object gets added to the list.
class Square():
    square_list = []

    def __init__(self, l):
        self.length = l
        self.square_list.append(self.length)

s1 = Square(1)
s2 = Square(2)
s3 = Square(3)
print(Square.square_list)


print("------------------------------------------")
# Change the Square class so that when you print a Square object, a message
# prints telling you the len of each of the four sides of the shape. For
# example, if you create a square with Square(29) and print it, Python should
# print '29 by 29 by 29 by 29'.
class Square():
    square_list = []

    def __init__(self, l):
        self.length = l
        self.square_list.append(self.length)

    def __repr__(self):
        l = self.length
        return f"{l} by {l} by {l} by {l}"

s1 = Square(1)
print(s1)


print("------------------------------------------")
# Write a function that takes two objects as parameters and returns True if
# they are the same object, and False if not.
def isSame(x, y):
    return x is y

print(isSame(s1,s1))
print(isSame(s1,s2))
