# Make hangman using everything we've learned so far

import random
import csv

div = "\n------------------------------------------------"

def hangman(word):
    win = False
    rletters = list(word)
    wletters = list()
    board = ["_"] * len(word)
    checkPunc(rletters, board)
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
    lb = leaderboard()
    print(div)
    name = input("What is your name? ").capitalize()
    print(div)
    print("Welcome to Hangman, " + name + "!")
    print("\n".join(stage))
    wrong = 0
    
    while wrong < 6:
        print("")
        print("Already guessed: " + " ".join(wletters))
        print("")
        print(" ".join(board))
        guess = input("Guess a letter: ").lower()
        if len(guess) > 1:
            print("*One letter at a time, please*")
            continue
        if guess in wletters:
            print("*You already guessed that...*")
            continue
        else:
            wletters.append(guess)
        if guess in rletters:
            print("*Good guess!*")
            check(guess, rletters, board)
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
        print("Sorry, you lost! It was '" + word + "'. Better luck next time!")

    writeLeaderboard(lb, name, win)

def checkPunc(rletters, board):
    check(" ", rletters, board)
    check("-", rletters, board)
    check(",", rletters, board)
    check(".", rletters, board)
    check("!", rletters, board)
    check("?", rletters, board)
    check("'", rletters, board)
    check(":", rletters, board)
    check("(", rletters, board)
    check(")", rletters, board)

def check(char, rletters, board):
    while char in rletters:
        i = rletters.index(char)
        board[i] = char
        rletters[i] = "$"

def leaderboard():
    lb = dict()
    with open("leaderboard.csv", "r") as f:
        r = csv.DictReader(f)
        print(div)
        print("LEADERBOARD:")
        linecount = 0
        for row in r:
            lb[row["name"]] = [int(row["wins"]), int(row["total"]), int(row["score"])]
            if linecount == 0:
                linecount += 1
            print(f'{linecount}) {row["name"]} ({row["wins"]}/{row["total"]} wins) - Score: {row["score"]}')
            linecount += 1
    return lb

def writeLeaderboard(lb, name, win):
    if name in lb:
        wins = lb[name][0]
        total = lb[name][1]
        score = lb[name][2]
        if win:
            wins += 1
            score += 10
        else:
            score -= 5
        total += 1
        lb[name] = [wins, total, score]
    else:
        if win:
            lb[name] = [1, 1, 10]
        else:
            lb[name] = [0, 1, -5]
    def getScore(data):
        return lb[data][2]
    s = sorted(lb, key=getScore, reverse=True)
    with open("leaderboard.csv", "w") as f:
        w = csv.writer(f, delimiter=",")
        w.writerow(["name","wins","total","score"])
        for key in s:
            w.writerow([key, lb[key][0], lb[key][1], lb[key][2]])

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
    if len(newWord) < 5:
        print("*Sorry, that word is too short*")
    else:
        with open("hardWords.csv", "a+", newline='') as f:
            w = csv.writer(f, delimiter="\n")
            w.writerow([newWord])

def chooseWord():
    word = ""
    words = []
    print("\nWORD OPTIONS:")
    with open("hardWords.csv", "r") as f:
        reader = csv.reader(f, delimiter="\n")
        for i,row in enumerate(reader):
            print(row[0] + ":   \t" + str(i))
            words.append(row[0])
        print("Some new word that I specify: n")
        choice = input("Type the number of the word you want to choose: ").lower()
        if choice == "n":
            while len(word) < 5:
                word = input("What word do you want your opponent to solve? ").lower()
                if len(word) < 5:
                    print("*That's not long enough*")
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
        print("Check the leaderboard: l")
        print("Add a new word: a")
        print("Quit: q")
        option = input("Type the letter of the option you want to choose: ").lower()
        if option == "s":
            startGame()
        elif option == "c":
            chooseWord()
        elif option == "l":
            leaderboard()
        elif option == "a":
            addWord()
        elif option != "q":
            print("Not an option")

options()
