# Chapter 22

# FizzBuzz
# Print numbers 1 to 100. For every number that is divisible by 3 print Fizz.
# For every number that is divisible by 5 print Buzz. If a number is divisible
# by both 3 and 5 print FizzBuzz.
def fizzbuzz():
    for i in range(1, 101):
        if i%3 == 0:
            if i%5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)
fizzbuzz()

print("---------------------------------------------")
# Twist:
# Print numbers 1 to 100. Given the dictionary below, print the corresponding value
# for each number that is divisible by the key in the dictionary.
dictionary = {3:'Chocolate', 4:'Cookies n cream', 5:'Red Velvet', 10:'Pazookie'}
def fizzbuzzTwist(dictionary):
    for i in range(1, 101):
        treats = str(i)
        for num in dictionary:
            if i%num == 0:
                treats = treats + " " + dictionary[num]
        print(treats)
fizzbuzzTwist(dictionary)  

print("---------------------------------------------")

# Palindrome
# Write a function that takes in a word and determines if it is a Palindrome.
# Palindrome = a word that is spelled the same way forward and backward.
# Example: racecar spelled backwards is racecar
def palindrome(word):
    word = word.lower()
    mid = int(len(word)/2)
    start = word[:mid]
    count = mid - 1
    if len(word)%2 == 0:
        end = word[mid:]
    else:
        end = word[mid+1:]
    while count >= 0:
        if start[count] != end[-1 - count]:
            return "Not a Palindrome"
        count -= 1
    return "Palindrome!"
print(palindrome("Hannah"))

print("---------------------------------------------")
# Anagram
# Write a function that takes in two words and determines if the words are an
# anagram of each other.
# Anagram = A word created by rearranging the letters of another word.
# Example: iceman and cinema
def anagram(one, two):
    for char in one:
        if char in two:
            two = two.replace(char, '$')
        else:
            return "Not an Anagram"
    return "Anagram!"
print(anagram("iceman", "cinema"))

print("---------------------------------------------")
# Character Count
# Write a function that takes in a word and returns the count of each character
# in the word.
# Example: The word cookie has 1 c, 2 o's, 1 k, 1 i, 1 e.
def charCount(word):
    w = word.lower()
    count = dict()
    for char in w:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    result = "The word " + word + " has"
    for letter in count:
        if count[letter] > 1:
            result = result + " " + str(count[letter]) + " " + letter + "'s,"
        else:
            result = result + " " + str(count[letter]) + " " + letter + ","
    result = result[:-1] + "."
    return result
print(charCount("Mississippi"))
