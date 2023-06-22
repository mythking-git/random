# Importing Fuctions
import random as r
import time as t

# Defining variables
global selNum, usedCards, selection, current, compare
dogsInfo, info, compCards, playerCards, current, compare = {}, [], [], [], [], []
selection = 0

#Reads file and assigns each dog it's 4 values and adds it to the dictionary
def fileread():
    with open("dogs.txt") as f:
        line = f.readline()
        line = line.strip()
        cnt=0
        while line:
            rdmExercise = r.randint(1,5)
            rdmFriend = r.randint(1,100)
            rdmInt = r.randint(1,10)
            rdmDrool = r.randint(1,10)
            dogsInfo[cnt] = [line,rdmExercise,rdmFriend,rdmInt,rdmDrool]
            line = f.readline()
            line = line.strip()
            cnt += 1 #20 minutes

#Menu with play/quit/incorrect checker
def menu():
    c = input("Type ""Play"" or ""Quit"": ")
    if c.lower() == "play" or c.lower() == "play game":
        t.sleep(1)
        game()
    elif c.lower() == "quit" or c.lower() == "quit game":
        print("\nProgram ending...")
        t.sleep(2)
        exit()
    else:
        print("\nInputted incorrect statement\n")
        menu() #40 minutes
    
# Gets player input
def game():
    try:
        global numCards
        numCards = 0
        numCards = int(input("\nInput the total amount of cards to be used, 4 < x < 30:  "))
        t.sleep(1)
        if (numCards % 2) == 0 and numCards > 3 and numCards < 31:
            print("\nCorrectly inputted value\n")
        else:  
            print("\nIncorrect Input\n")
            game()
    except:
        print("\nIncorrect input\n")
        game() #50 minutes
    split()

#Splits the cards between the player and the computer
def split():
    loop = 0
    global usedCards
    usedCards = []
    while len(usedCards) <= (numCards/2) and loop < (numCards/2):
        loop += 1
        random = r.choice(dogsInfo)
        if random != any(usedCards):
            random = r.choice(dogsInfo)
            playerCards.append(random)
    while len(usedCards) < (numCards) and loop < (numCards):
        loop += 1
        random = r.choice(dogsInfo)
        if random != any(usedCards):
            random = r.choice(dogsInfo)
            compCards.append(random) #90 minutes
    gameplay()

# Prints what the player has selected
def selInput():
    global selNum
    selection = str(input("Select exercise, friendliness, intelligence or drool: "))
    lowered = str(selection.lower())
    if lowered == "exercise" or lowered == "friendliness" or lowered == "intelligence" or lowered == "drool":
        if selection == "exercise":
            selNum = 1
            print("\nYour Cards Exercise: {0}\nvs\nComputer's Exercise: {1}".format(current[selNum],compare[selNum]))
        if selection == "friendliness":
            selNum = 2
            print("\nYour Cards Friendliness: {0}\nvs\nComputer's Friendliness: {1}".format(current[selNum],compare[selNum]))
        if selection == "intelligence":
            selNum = 3
            print("\nYour Cards Intelligence: {0}\nvs\nComputer's Intelligence: {1}".format(current[selNum],compare[selNum]))
        if selection == "drool":
            selNum = 4
            print("\nYour Cards Drool: {0}\nvs\nComputer's Drool: {1}".format(current[selNum],compare[selNum]))
    else:
        print("Incorrect Input")
        selInput()

# Prints the players card
def cardPrint():
    top = "/"+("-"*46)+"\\ \n"
    btm ="\\"+("-"*46)+"/ \n"
    card = "| Current Card: " + str(current[0])
    card = "| Current Card: " + str(current[0]) + (" "*(47-len(card))) + "| \n"
    exercise = "| Exercise: " + str(current[1]) + "/5"
    exercise = "| Exercise: " + str(current[1]) + "/5" + (" "*(47-len(exercise))) + "| \n"
    friend =  "| Friendliness: " + str(current[2]) + "/100"
    friend = "| Friendliness: " + str(current[2]) + "/100" + (" "*(47-len(friend))) + "| \n"
    intel = "| Intelligence: " + str(current[3]) + "/10"
    intel = "| Intelligence: " + str(current[3]) + "/10" + (" "*(47-len(intel))) + "| \n"
    drool = "| Drool: " + str(current[4]) + "/10"
    drool = "| Drool: " + str(current[4]) + "/10" + (" "*(47-len(drool))) + "| \n"
    print(top + card + exercise + friend + intel + drool +btm)

# Calculates who has won the round
def gameplay():
    global current
    global compare
    playerScore = 0
    compScore = 0
    while len(playerCards) > 0:
        current = playerCards.pop()
        compare = compCards.pop()
        cardPrint()
        selInput()
        t.sleep(3)
        if compare[selNum] < current[selNum]: # 140 minutes
            playerScore += 1
            print("\nYou won this round: \n" +"Your score: " + str(playerScore) + "\nComputer's Score: " + str(compScore) + "\n")
        elif compare[selNum] > current[selNum]:
            compScore += 1
            print("\nYou lost this round: \n" +"Your score: " + str(playerScore) + "\nComputer's Score: " + str(compScore) + "\n")
        elif compare[selNum] == current[selNum]:
            print("\nYou drew. \n" +"Your score: " + str(playerScore) + "\nComputer's Score: " + str(compScore) + "\n")
        else:
            print("Error",current[selNum],compare[selNum])        
        t.sleep(3)
    print("Game ended") # 150 minutes

fileread()
#for i in dogsInfo:
#    print(dogsInfo[i][0],"Exercise:",dogsInfo[i][1],",Friendliness:",dogsInfo[i][2],",Intelligence:",dogsInfo[i][3],",Drool:",dogsInfo[i][4])
menu()
