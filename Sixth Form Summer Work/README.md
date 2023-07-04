# Problem 1

1. Write an program to:
    - Ask the user to input
        - Their first name
        - Their surname
        - A date, in the format DD/MM/YYYY
    - The program should then output a customer ID as follows:
        - The date in the format YYYYMMDD, then the first three letters of the
        surname, then the first initial, then the length of their first name. All letters
        should be in capitals
        - For example, John Smith, 27/05/2017 would give 20170527SMITHJ4
    - The program should validate any inputs and keep asking for inputs until the user
    enters correct details or types “quit” at any point

## Pseudocode Plan
```
function checks:
    while inputs_not_valid:
        take inputs 
        check length and characters in first and last name
        check length, all digits, and in correct form for date
        
    concatenate and form final ID
    return value
    
call function check and store to variable
output customer ID
```

# Problem 2

2. Write a program to:
   - Ask the user to input
        - The name of a product
        - Its cost in pounds
        - The program should keep asking for inputs until the user types “None”
    - The program should then output:
        - The name and price of the most expensive item
        - The name and price of the least expensive item
        - The average price of the items
        - The total cost of the items
            - Items over £50 get a 5% discount
            - VAT is added at the end at 20%
    - The program should validate any inputs


## Pseudocode Plan
```
while loop until == none
    name
    cost
    if name not words:
        go to start of loop
    if cost not float:
        go to start of loop
    
list max and min
average
outputs
```
