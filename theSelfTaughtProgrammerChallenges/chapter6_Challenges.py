# Print every character in the string "Camus".
word = "Camus"
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])


print("------------------------------------------------------------")
# Write a program that collects two strings from a user, inserts them into the
# string "Yesterday I wrote a [response_one]. I sent it to [response_two]!",
# and prints a new string.
r1 = input("Enter a noun: ")
r2 = input("Enter a person's name: ")
story = "Yesterday I wrote a {}. I sent it to {}!".format(r1, r2)
print(story)


print("------------------------------------------------------------")
# Use a method to make the string "aldous Huxley was born in 1984."
# grammatically correct by capitalizing the first letter in the sentence.
accurate = "aldous Huxley was born in 1984."
p1 = accurate[:3].capitalize()
p2 = accurate[3:]
accurate = p1 + p2
print(accurate)


print("------------------------------------------------------------")
# Take the string "Where now? Who now? When now?" and call a method that returns
# a list that looks like: ["Where now?", "Who now?", "When now?"].
questions = "Where now? Who now? When now?".split("? ")
questions[0] = questions[0] + "?"
questions[1] = questions[1] + "?"
print(questions)


print("------------------------------------------------------------")
# Take the list ["The", "fox", "jumped", "over", "the", "fence", "."] and turn
# it into a grammatically correct string. There should be a space between each
# word, but no space between the word fence and the period that follows it.
wordList = ["The", "fox", "jumped", "over", "the", "fence", "."]
result = " ".join(wordList)
result = result[:-2] + result[-1:]
print(result)


print("------------------------------------------------------------")
# Replace every instance of "s" in "A screaming comes across the sky." with a
# dollar sign.
replacement = "A screaming comes across the sky.".replace("s", "$")
print(replacement)


print("------------------------------------------------------------")
# Use a method to find the first index of the character "m" in the string
# "Hemingway".
i = "Hemingway".index("m")
print(i)


print("------------------------------------------------------------")
# Find dialogue in your favorite book (containing quotes) and turn it into
# a string.
quote = '"Hello", says the boy.'
print(quote)


print("------------------------------------------------------------")
# Create the string "three three three" using concatenation, and then again
# using multiplication.
three = "three "
concat = three + three + three
multiple = three * 3
print(concat + "- and - " + multiple)


print("------------------------------------------------------------")
# Slice the string "It was a bright cold day in April, and the clocks were
# striking thirteen." to only include the characters before the comma.
longStr = """It was a bright cold day in April, and the clocks were
striking thirteen."""
longStr = longStr[:longStr.index(",")]
print(longStr)
