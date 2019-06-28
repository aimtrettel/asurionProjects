# Make hangman using everything we've learned so far
# To Do: make leaderboard, keep track of wrong letters

import random
import csv

div = "\n------------------------------------------------"

def hangman(word):
    win = False
    rletters = list(word)
    board = ["_"] * len(word)
    
    stage1 = [
        "___________",
        "|     |    ",
        "|     O    ",
        "|          ",
        "|          ",
        "|          ",
        "|          ",
        "|__________"
    ]
    stage2 = [
        "___________",
        "|     |    ",
        "|     O    ",
        "|     |    ",
        "|     |    ",
        "|          ",
        "|          ",
        "|__________"
    ]
    stage3 = [
        "___________",
        "|     |    ",
        "|     O    ",
        "|    /|    ",
        "|   / |    ",
        "|          ",
        "|          ",
        "|__________"
    ]
    stage4 = [
        "___________",
        "|     |    ",
        "|     O    ",
        "|    /|\   ",
        "|   / | \  ",
        "|          ",
        "|          ",
        "|__________"
    ]
    stage5 = [
        "___________",
        "|     |    ",
        "|     O    ",
        "|    /|\   ",
        "|   / | \  ",
        "|    /     ",
        "|  _/      ",
        "|__________"
    ]
    stage6 = [
        "___________",
        "|     |    ",
        "|     O    ",
        "|    /|\   ",
        "|   / | \  ",
        "|    / \   ",
        "|  _/   \_ ",
        "|__________"
    ]
    stage = [
        "___________",
        "|     |    ",
        "|          ",
        "|          ",
        "|          ",
        "|          ",
        "|          ",
        "|__________"
    ]
    dead_stages = [
        stage1,
        stage2,
        stage3,
        stage4,
        stage5,
        stage6
    ]
    win_graphic = [
        " /-------\ ",
        "| Thanks! |",
        " \----v--/ ",
        "     O     ",
        "    /|\/   ",
        "   / |     ",
        "    / \    ",
        "___/___\___"
        ]
    print(div)
    name = input("What is your name? ").capitalize()
    print(div)
    print("Welcome to Hangman, " + name + "!")
    print("\n".join(stage))
    wrong = 0
    
    while wrong < 6:
        print("")
        print(" ".join(board))
        guess = input("Guess a letter: ").lower()
        if guess in rletters:
            print("Good guess!")
            while guess in rletters:
                i = rletters.index(guess)
                board[i] = guess
                rletters[i] = "$"
        else:
            wrong += 1
            stage = dead_stages[wrong -1]
            print("\n".join(stage))
        if "_" not in board:
            win = True
            print("")
            print("\n".join(win_graphic))
            print("Well done! You won!")
            break

    if win == False:
        print("Sorry, you lost! The word was " + word + ". Better luck next time!")


def startGame():
    words = []
    with open("words.csv", "r") as f:
        reader = csv.reader(f, delimiter="\n")
        for row in reader:
            words.append(row[0])
    r = random.randint(0,len(words))
    hangman(words[r])

def addWord():
    newWord = input("What word would you like to add? ").lower()
    with open("words.csv", "a+", newline='') as f:
        w = csv.writer(f, delimiter="\n")
        w.writerow([newWord])

def chooseWord():
    word = ""
    words = []
    print("\nWORD OPTIONS:")
    with open("words.csv", "r") as f:
        reader = csv.reader(f, delimiter="\n")
        for i,row in enumerate(reader):
            print(row[0] + ":   \t" + str(i))
            words.append(row[0])
        print("Some new word that I specify: n")
        choice = input("Type the number of the word you want to choose: ").lower()
        if choice == "n":
            word = input("What word do you want your opponent to solve? ").lower()
        else:
            word = words[int(choice)]
    i = 50
    while i > 0:
        print("-----")
        i -= 1
    hangman(word)

def options():
    option = ""
    while option != "q":
        print(div)
        print("MAIN MENU - HANGMAN")
        print("Start a game of hangman with the computer: s")
        print("Choose a word for your opponent: c")
        print("Add a new word: a")
        print("Quit: q")
        option = input("Type the letter of the option you want to choose: ").lower()
        if option == "s":
            startGame()
        elif option == "c":
            chooseWord()
        elif option == "a":
            addWord()
        elif option != "q":
            print("Not an option")

options()
