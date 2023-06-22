#Menu with check/gen/quit/incorrect checker
def menu():
    user_request = input("Type ""Check Password"", ""Generate Password"", or ""Quit"": ")
    if user_request.lower() == "check password":
        playerInputted = True
        checkPassword(playerInputted)
    elif user_request.lower() == "generate password":
        generatePassword()
    elif user_request.lower() == "quit":
        print("\nProgram ending...")
        exit()
    else:
        print("\nInputted incorrect statement\n")
        menu()

def checkPassword(playerInputted):
    if playerInputted == True:
        password = input("Enter your password between 8 and 24 characters long: ")
    if len(password) >= 8 and len(password) <= 24:
        print("Length is correct")
        allowedCharCheck(password,playerInputted)
    else:
        print("Length is incorrect")
        checkPassword(playerInputted)

def allowedCharCheck(password,playerInputted):
    # LOWER, UPPER, DIGIT, SPECIALCHARACTER
    flagList = [False,False,False,False,0,""]
    for char in password:
        if char in ("abcdefghijklmnopqrstuvwxyz"):
            flagList[0] = True
        elif char in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            flagList[1] = True
        elif char in ("0123456789"):
            flagList[2] = True
        elif char in ("!£$%^&*()-_=+"):
            flagList[3] = True
        else:
            print("Unpermitted symbol/character used")
            checkPassword()
    if playerInputted == True:
        scoreCalculation(flagList,password)

def scoreCalculation(flagList,password):
    QWERTY = ["qwe","wer","ert","rty","tyu","yui","iop","asd","sdf","dfg","fgh","hjk","jkl","zxc","xcv","cvb","vbn","bnm"]
    flagList[4] += sum(flagList[0:3])*5 + len(password)
    if sum(flagList[0:3]) == 4:
        flagList[4] += 10
        print(passwordScore)
    # lower = true, upper = true, digit = false, special = false | Only upper and lower
    elif flagList[0] and flagList[1] and flagList[2] == False and flagList[3] == False:
        flagList[4] -= 5
    # lower = false, upper = false, digit = true, special = true | Only digits
    elif flagList[0] == False and flagList[1] == False and flagList[2] and flagList[3] == False:
        flagList[4] -= 5
    # lower = true, upper = true, digit = false, special = false | Only special characters
    elif flagList[0] == False and flagList[1] == False and flagList[2] == False and flagList[3]:
        flagList[4] -= 5
    listPassword = list(password.lower())
    consecutiveChar = 0
    for q in range(len(password)-2):
        letters=[]
        letters.append(listPassword[q]+listPassword[q+1]+listPassword[q+2])
        if letters[0] in QWERTY:
            consecutiveChar += 1
            flagList[4] -= 5
    if flagList[4] < 0:
        flagList[5]= "Poor Strength"
    if flagList[4] > 20:
        flagList[5]= "Strong Password"
    else:
        flagList[5]= "Medium Strength"
    finalScore(password,flagList,consecutiveChar)
    
def finalScore(password,flagList,consecutiveChar):
    print("\nAdditions:-"+" "*28+"Points"+"\nPassword length is",len(password)," "*18,len(password))
    if flagList[0]:
        print("At least one lower case character:       5")
    if flagList[1]:
        print("At least one upper case character:       5")
    if flagList[2]:
        print("At least one digit:                      5")
    if flagList[3]:
        print("At least one symbol:                     5")
    if sum(flagList[0:3]) == 4:
        print("All of the above: 10")
    print("\nSubtraction:-")
    if flagList[0] and flagList[1] and flagList[2] == False and flagList[3] == False:
        print("Only upper and lowercase characters:    -5")
    if flagList[0] == False and flagList[1] == False and flagList[2] and flagList[3] == False:
        print("Only digits:                            -5")
    if flagList[0] == False and flagList[1] == False and flagList[2] == False and flagList[3]:
        print("Only symbols:                           -5")
    if flagList[4] < 0:
        print("Consecutive QWERTY characters:         ",consecutiveChar*-5)
    print("\nResult:",flagList[5],"          Score:",flagList[4])
    
menu()
