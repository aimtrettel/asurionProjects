# Create a list of your favorite musicians.
musicians = ["Drake White", "Zac Brown Band", "Luke Combs"]

print(musicians)


# Create a list of tuples, with each tuple containing the longitude and
# latitude of somewhere you've lived or visited.
locations = [(38.8121, 77.6364,), (38.5923, 89.9110,), (38.8339, 104.8214,)]

print(locations)


# Create a dictionary that contains different attributes about you: height,
# favorite color, favorite author, etc.
me = {"height": 5.4, "favorite color": "green", "favorite author": "C.S. Lewis"}

print(me)


# Write a program that lets the user ask your height, favorite color, or
# favorite author, and returns the result from the dictionary you created
# in the previous challenge.
question = input("What would you like to know about me? ")
if(question in me):
    print(me[question])
else:
    print("Answer not found")


# Create a dictionary mapping your favorite musicians to a list of your
# favorite songs by them.
songs = {"Drake White": ["Make Me Look Good Again", "Take Me As I Am"],
         "Zac Brown Band": ["Remedy", "Chicken Fried", "My Old Man"],
         "Luke Combs": ["Beautiful, Crazy", "Houston, We've Got a Problem"]}

print(songs)


# Lists, tuples, and dictionaries are just a few of the containers built into
# Python. Research Python sets (a type of container). When would you use a set?
        # Use a set when you want to do math stuff
