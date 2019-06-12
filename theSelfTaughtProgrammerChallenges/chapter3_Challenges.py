# Print three different strings.
print("Aimee")
print("Elizabeth")
print("Trettel")


# Write a program that prints a message if a variable is less than 10,
# and different message if the variable is greater than or equal to 10.
a = 30
if(a < 10):
      print("Less than 10")
else:
      print("Greater than or equal 10")


# Write a program that prints a message if a variable is less than or equal
# to 10, another message if the variable is greater than 10 but less than or
# equal to 25, and another message if the variable is greater than 25.
if(a <= 10):
      print("Less than or equal 10")
elif(a > 10 and a <= 25):
      print("Between 10 & 25")
else:
      print("Greater than 25")


# Create a program that divides two variables and prints the remainder.
b = 4
result = a % b
print(result)


# Create a program that takes two variables, divides them,
# and prints the quotient.
result = a // b
print(result)


# Write a program with a variable "age" assigned to an integer that prints
# different strings depending on what integer "age" is.
age = 21
if(age <= 12):
    print("Where are your parents?")
elif(age < 18):
    print("Shouldn't you be in school?")
elif(age < 21):
    print("Welcome to adulthood! But no bars for you...")
else:
    print("Now you're just getting old from here... go grab a beer")
