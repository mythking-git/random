  # -- Packages -- #

import random

  # -- Subroutines -- #

# Loading the Menu, checks the function that user would like to complete, validation implimented.
def openMenu():
    guess = input("Please input 4 digit guess with no duplicates (or ""Exit""): ")
    guess_list = []

    if guess.lower() == "exit":
        print("\nProgram ending...")
        exit()

    else:
        try:
            # Checks if input is not a string
            int(guess)

            # Checks length
            if len(guess) != 4:
                raise ValueError

            # Converts from string to list
            for i in range(len(guess)):
                guess_list.append(int(guess[i]))

            # Checks for duplicates by comparing set lengths
            if len(guess) != len(set(guess)):
                raise ValueError

            # Debugging
            #print("\nPlayer's value: ", str(guess_list))
            
            cows_and_bulls(guess_list)         
            

        # If the code above raises ValueError it recalls the function
        except ValueError:
            guess = ""
            guess_list = []
            print("\nIncorrect Input\n")
            openMenu()
        
        

def generateNumber(list):
    
    # Repeats until machines value is of the correct length
    while len(num) != 4:

        # Generates a random value
        random_integer = random.randint(0,9)

        # Checks if generated value is a duplicate
        if random_integer in list:
            print(list)
            generateNumber(list)
            
        # Adds values to the computer's number
        else:
            list.append(random_integer)
            num.append(random_integer)
    
    # Returns the final 4 digit number
    return num
            

def cows_and_bulls(guess_list):

    guesses,cows,bulls = 0,0,0

    # Checks for cows
    for i in range(len(generated_number)):
        if generated_number[i] == guess_list[i]:
            bulls = bulls + 1
        elif guess_list[i] in generated_number:
            cows = cows + 1
    
    guesses = guesses + 1
    
    # Adds current guess to previous guesses
    guess = [str(guess_list[0])+str(guess_list[1])+str(guess_list[2])+str(guess_list[3]),bulls,cows]
    prev_guess.append(guess)

    print("\nGuesses:\n")
    
    # Prints all previous guesses
    for item in range(len(prev_guess)):
        print("Guess",str(item+1)+":","\""+str(prev_guess[item][0])+"\"","Cows:",str(prev_guess[item][1]),"Bulls:",str(prev_guess[item][2]))
    
    # Ends program if guess is correct
    if generated_number == guess_list:
        print("You guessed the number correctly in",guesses,"guesses")
        exit()
    
    print("\n")
    
    openMenu()

  # -- Main Code -- #

used_values, num, prev_guess = [], [], []

generated_number = generateNumber(used_values)

openMenu()



