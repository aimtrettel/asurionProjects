# Print each item in the following list: ["The Walking Dead", "Entourage",
# "The Sopranos", "The Vampire Diaries"].
shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for show in shows:
    print(show)


print("--------------------------------------------------------------------")
# Print all the numbers from 25 to 50.
for i in range(25, 51):
    print(i)


print("--------------------------------------------------------------------")
# Print each item in the list from the first challenge and their indexes.
for i, show in enumerate(shows):
    print(str(i) + ": " + show)


print("--------------------------------------------------------------------")
# Write a program with an infinite loop (with the option to type q to quit) and
# a list of numbers. Each time through the loop ask the user to guess a number
# on the list and tell them whether or not they guessed correctly.
numbers = [1, 2, 3, 4, 5, 6]
while True:
    a = input("Pick a number (or q to quit): ")
    if(a == "q"):
        break
    if(int(a) in numbers):
        print("Correct!")
    else:
        print("Sorry, that's not in the list")


print("--------------------------------------------------------------------")
# Multiply all the numbers in the list [8, 19, 148, 4] with all the numbers in
# the list [9, 1, 33, 83], and append each result to a third list.
one = [8, 19, 148, 4]
two = [9, 1, 33, 83]
result = []
for i in one:
    for j in two:
        result.append(i * j)

print(result)
