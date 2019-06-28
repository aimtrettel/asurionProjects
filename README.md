# Python Cheat Sheet
To make a comment use a hash tag:

    # This is a comment.
    
To print use the built-in print function:

    print("Hello World!")
    
**Important**: Python uses proper spacing to distinguish blocks of code
(tab or 4 spaces)

## Data Types
* string: str ... "This is a string"
* integer: int ... 87
* floating-point: float ... 87.6
* booleans: bool ... True
* NonType: None

Python does not require you to specify the data type when making variable
declarations. For example:

    a = 100
    print(a)
    
>> 100

## Variable Operations

#### Addition: 

    z = x + y
    z = z + 1
    z += 1
    
#### Subtraction:

    z = x - y
    z = z - 1
    z -= 1
    
#### Multiplication:

    z = x * y      # Multiplication
    z = x ** y     # Exponenet
    
#### Division:

    z = x / y      # Division
    z = x // y     # Integer division/floored quotient
    z = x % y      # Modulo/remainder
    
#### Comparison Operations:

    >       # Greater Than
    <       # Less Than
    >=      # Greater Than or Equal To
    <=      # Less Than or Equal To
    ==      # Equal
    !=      # Not Equal
    
#### Logical Operations:

    and     # (True and True) would return True
    or      # (True or False) would return True
    not     # (not True) would return False
    
## Conditional Statements

    if x == 2:
        print("The number is 2.")
    elif x == 5:
        print("The number is 5.")
    else:
        print("I don't know this number.")
        
## Functions
Use keyword *def* to define your function and then give your function a
name & parameters. For example:

    def functionName(x):
        return x + 1
        
    functionName(2)
>> 3

#### Built-in Functions:
* len(x) - returns the length of object, x
* str(x) - returns the object, x, as a string
* int(x) - returns the object, x, as an integer
* float(x) - returns the object, x, as a floating-point number
* input(x) - prints the prompt, x, and returns the user's input

#### Required & Optional Parameters:
Python lets you specify whether a parameter is required or optional by
allowing you to set a default value for a parameter.

###### Required Parameters:

    def functionName(x, y, z):
    
###### Optional Parameters:

    def functionName(x = 1, y = 2, z = 3):
    
## Variable Scope
**Global Variable** - a variable with global scope can be read or written
to from anywhere in your program

**Local Variable** - a variable with local scope can only be read or written
to from within the class of function that it is in

Use keyword *global* when writing to a global variable from within a function

    x = 2
    
    def f():
        global x
        x += 1
        print(x)
        
    f()
>> 3
        
## Error Handling

    y = input("Give a value for y: ")
    
    try:
        x = int(y)
    except ValueError:
        print("y must be a number")
>> Give a value for y: **Python**

>> y must be a number

##### Python Exceptions:
* SyntaxError: EOL while scanning string literal
* ZeroDivisionError: division by zero
* IndentationError: unexpected indent
* ValueError: invalid literal for int() with base 10: 'exampleString'

## Containers

### Lists

* a container that stores objects in a specific order
* iterable
* mutable


    list = []
    list = list()
    
find an object in a list by adding brackets with the object's index: list[0]

use *append()* to add to a list

use *pop()* to remove the last item from a list

add two lists with the addition operator

use keyword *in* to check if an item is in a list

use keyword *not* paired with *in* to check if an item is not in a list

### Tuples

* a container that stores objects in a specific order
* immutable
* iterable


    tuple = ()
    tuple = tuple()
    
find an object in a list by adding brackets with the object's
index: tuple[1]

use keywords *in* and *not* just like lists

### Dictionaries

* a container that maps a key to a value


    dictionary = {}
    dictionary = dict()
    
add a value using the following format:

    dictionary["key1"] = "value1"
    dictionary["key2"] = "value2"
>> {"key1":"value1", "key2":"value2"}

use keywords *in* and *not* just like lists

Containers can contain containers inside of them.

### Strings

* strings are immutable
* use an index to look up a character, indexes start at 0
* a **negative index** can be used to look up items from right to left
where [-1] gives the last character in a string


    name = "Elizabeth"
    name[0]     // = E
    name[2]     // = i
    name[-1]    // = h
    name[-2]    // = t

* triple quotes can be used to surround a string that has multiple lines


    """line 1
       line 2
       line 3
    """
    
* use '+' to add strings together


    "string1" + "string2"
    
>> string1string2

* use the asterisk to multiply strings


    "string1" * 2
    
>> string1string1

#### Built-in Functions for Strings

**.upper()** - turns string to all upper case characters

**.lower()** - turns string to all lower case characters

**.capitalize()** - capitalizes the first letter of a sentence

**.format(x)** - will insert the string, x, into the string to replace empty {}

    "Hello, my name is {}".format("Aimee")
    
>> 'Hello, my name is Aimee'

**.split(x)** - splits a string at each string, x, and puts them into a list

    "blue, pink, purple".split(", ")
    
>> ["blue", "pink", "purple"]

**.join(x)** - adds string, x, between the characters of the string

    ".".join("python")
>> p.y.t.h.o.n

**.strip()** - strips the string of excess white space

    "      Python    ".strip()
>> 'Python'

**.replace(x, y)** - when passed two arguments x & y, it will replace every
occurrence of x with y

    "All animals are equal.".replace("a", "@")
>> 'All @nim@ls @re equ@l.'

**.index(x)** - returns the index of the first occurrence of x in the string

    "animals".index("m")
>> 3

* use the keyword *in* to check if a string contains another string

* escape characters within strings by using the backslash (\)

* \n in a string creates a new line

* use the syntax string[x:y] to slice a string from index x up to index y
(can be used on Lists as well)

## Loops

#### For-loops

* for-loops are used to iterate through an iterable (string, list, etc.)


    name = "Ted"
    for character in name:
        print(character)
>> T

>> e

>> d

* you can also have an index variable in a for-loop by using enumerate(x):


    tv = ["GOT", "Narcos", "Vice"]
    for i, show in enumerate(tv):
        new = tv[i]
        new = new.upper()
        tv[i] = new
        
    print(tv)
>> ['GOT', 'NARCOS', 'VICE']

* or by using range(x, y):


    for i in range(1, 11):
        print(i)
>> 1

...
>> 9

>> 10

#### While-loops

* while-loops are used to run a block of code as long as a condition is true


    x = 3
    while x > 0:
        print(x)
        x -= 1
    print("Happy New Year!")
>> 3

>> 2

>> 1

>> 'Happy New Year!'

* **Note:** writing 'while True:' will make an **infinite loop** unless you use a
break statement

#### Break

* a break statement is used to terminate a loop


    while True:
        a = input("Guess a number: ")
        if a == '87':
            break
        else
            print("That's not the right number!"
            
#### Continue
            
* a continue statement stops the current iteration & moves onto the next one


    for i in range(1, 6):
        if i == 3:
            continue
        print(i)
>> 1

>> 2

>> 4

>> 5

#### Nested Loops

* you can combine loops by putting, or 'nesting', one loop inside another


    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    added = []
    for i in list1:
        for j in list2:
            added.append(i + j)
            
    print(added)
>> [5, 6, 7, 6, 7, 8, 7, 8, 9]

## Modules

* another name for a python file with code in it

* you can import a module using keyword *import* to use variables and
functions from it

#### Built-in Modules:

* math

* random

* statistics

* keyword


    import math
    math.pow(2, 3)
>> 8.0

**Create your own module by:**

* create a python file

* save a file

* import the file into another file located in the same folder

#### Files

* python has built-in functions made to manipulate file objects

* first step is to open a file using the *open()* function

* the *write(x)* function lets you write x to a file

* the *read()* function lets you read from a file

* you must close a file with the *close()* function

#### Open file

* the *open* function takes a file and a file mode and returns a file object

* Here are some modes that you can open a file in:
    * "r" - opens a file for reading only
    * "w" - opens a file for writing only; overwrites the file if it already
    exists; if it doesn't exist, creates a new file
    * "w+" - opens a file for reading and writing; overwrites the file if it already
    exists; if it doesn't exist, creates a new file
    

    st = open("st.txt", "w")
    st.write("Hi from Python!")
    st.close()
    
#### Automatically close file

* to automatically close a file without using the *close()* function, open
your file using a **with-statement**


    with open("st.txt", "w") as f:
        f.write("Hi from Python!")
        
* this will automatically close the file once the code inside the
with-statement executes

#### CSV files

* python has a built-in module for working with CSV files

* you can use the *open()* function to open a file and then use the *writer()*

* use the function *writerow()* to write to the csv object


    import csv
    
    with open("st.csv", "w", newline='') as f:
        w = csv.writer(f, delimiter=",")
        w.writerow(["one", "two", "three"])
        w.writerow(["four", "five", "six"])
>> one,two,three

>> four,five,six

* the csv module also has a function for reading a CSV file: *reader()*

* the *reader()* function returns an iterable of the rows in the csv file


    import csv
    
    with open("st.csv", "r") as f:
        r = csv.reader(f, delimiter=",")
        for row in r:
            print(",".join(row))
>> one,two,three

>> four,five,six