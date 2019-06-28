# Make hangman using everything we've learned so far

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
    dead_stage2 = [
        "___________",
        "|     |    ",
        "|     O    ",
        "|     |    ",
        "|     |    ",
        "|          ",
        "|          ",
        "|__________"
    ]
    dead_stage3 = [
        "___________",
        "|     |    ",
        "|     O    ",
        "|    /|    ",
        "|   / |    ",
        "|          ",
        "|          ",
        "|__________"
    ]
    dead_stage4 = [
        "___________",
        "|     |    ",
        "|     O    ",
        "|    /|\   ",
        "|   / | \  ",
        "|          ",
        "|          ",
        "|__________"
    ]
    dead_stage5 = [
        "___________",
        "|     |    ",
        "|     O    ",
        "|    /|\   ",
        "|   / | \  ",
        "|    /     ",
        "|  _/      ",
        "|__________"
    ]
    dead_stage6 = [
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
        dead_stage1,
        dead_stage2,
        dead_stage3,
        dead_stage4,
        dead_stage5,
        dead_stage6
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
    print("Welcome to Hangman!")
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
            print("choose word")
        elif option == "a":
            addWord()
        elif option != "q":
            print("Not an option")

options()
