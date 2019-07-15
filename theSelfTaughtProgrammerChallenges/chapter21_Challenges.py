# Reverse the string "yesterday" using a stack.
word = "yesterday"
start = list(word)
result = list()
while len(start) > 0:
    result.append(start.pop())

print(result)


# Use a stack to create a new list with the items in the following list
# reversed: [1, 2, 3, 4, 5].
original = [1, 2, 3, 4, 5]
result2 = list()
while len(original) > 0:
    result2.append(original.pop())

print(result2)
