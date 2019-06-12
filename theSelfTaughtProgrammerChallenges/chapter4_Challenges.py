# Write a function that takes a number as an input, and
# returns that number squared.
def one(x):
    """
    Returns x squared.
    :param x: int.
    :return: int result of the input squared
    """
    return x**2

print(one(5))


# Create a function that accepts a string as a parameter and prints it.
def two(s):
    """
    Prints s.
    :param s: string.
    """
    print(s)

two("Aimee")


# Write a function that takes three required parameters
# and two optional parameters.
def three(a, b, c, d = 4, e = 5):
    """
    Prints (a + b + c + d + e).
    :param a: int.
    :param b: int.
    :param c: int.
    :param d: int (optional).
    :param e: int (optional).
    """
    print(a + b + c + d + e)

three(1, 2, 3)


# Write a program with two functions. The first function should take an
# integer as a parameter and return the result of the integer divided by 2.
# The second function should take an integer as a parameter and return the
# result of the integer multiplied by 4. Call the first function, save the
# result as a variable, and pass it as a parameter to the second function.
def fourOne(x):
    """
    Returns x / 2.
    :param x: int.
    :return: int quotient of x / 2.
    """
    return x / 2

def fourTwo(y):
    """
    Returns y * 4.
    :param y: int.
    :return: int product of y * 4.
    """
    return y * 4

result = fourOne(4)
print(fourTwo(result))


# Write a function that converts a string to a float and returns the result.
# Use exception handling to catch the exception that could occur.
def five(val):
    """
    Prints whether val is good input.
    :param val: str.
    """
    try:
        result = float(val)
        print("Oh good! Thanks!")
    except ValueError:
        print("OH NO! Bad input!")

i = input("Give a string to change into a float: ")
five(i)


# Add a docstring to all of the functions you wrote in challenges 1-5.
