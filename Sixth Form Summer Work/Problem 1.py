# Indef loop function to check for correct inputs
def inputCheck():
    
    inputFlag = False
    
    # while True works here, but flag makes it more reuseable
    while not inputFlag:

        # Inputs
        first_name = input("First Name: ")
        surname = input("Surname: ")
        input_date = input("Date (DD/MM/YYYY): ")

        # Checks for forward slash to meet form
        if not "/" in input_date:
            print("Input Date is invalid, form 'DD/MM/YYYY'\n")
            inputCheck()

        # Splits string date to list ["DD","MM","YYYY"]
        # through forward slash selector
        split_date = input_date.split("/")
        
        # Checks list lengths to ensure only 2 /'s are in the input
        if len(split_date) != 3:
            print("Input Date is invalid, form 'DD/MM/YYYY'\n")
            inputCheck()
        
        # Concatenates list into form "YYYYMMDD"
        joined_date = split_date[2] + split_date [1] + split_date[0]
        
        print(joined_date,joined_date.isnumeric())
        
        # Checks that length in 8 characters long and all integers
        if len(joined_date) != 8:
            print("Input Date is invalid, form 'DD/MM/YYYY'\n")
            inputCheck()
            
        if len(joined_date) != 8:
            print("Input Date is invalid, form 'DD/MM/YYYY'\n")
            inputCheck()

        # Checks that first name is alphanumeric (letters)
        if not first_name.isalpha():
           print("First Name is invalid, characters only\n")
           inputCheck()

        # Checks that surname is alphanumeric (letters)
        elif not surname.isalpha():
           print("Surname is invalid, characters only\n")
           inputCheck()

        else:
           # Not strictly necessary 
           inputFlag = True
           
           # Forms final output ID
           customerID = joined_date + surname.upper() + first_name[0].upper() + str(len(first_name))
           return customerID
       
customerID = inputCheck()

print(customerID)
