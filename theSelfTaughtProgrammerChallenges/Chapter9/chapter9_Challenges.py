import csv

# Find a file on your computer and print its contents using Python.
with open("one.txt", "r") as f:
    print(f.read())


# Write a program that asks a user a question, and saves their answer to a file.
answer = input("What is your favorite color? ")
with open("colors.txt", "w") as f2:
    f2.write(answer)


# Take the items in this list of lists: [["Top Gun", "Risky Business",
# "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day",
# "Man on Fire", "Flight"]] and write them to a CSV file. The data from each
# list should be a row in the file, with each item in the list separated by
# a comma.
motherOfLists = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic",
    "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
with open("movies.csv", "w") as f3:
    scribe = csv.writer(f3, delimiter=",")
    for row in motherOfLists:
        scribe.writerow(row)
