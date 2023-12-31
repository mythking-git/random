import random

def MakeSudoku():
    Grid = [[0 for x in range(15)] for y in range(15)]
            
    for i in range(15):
        for j in range(15):
            Grid[i][j] = 0
            
    # The range here is the amount
	# of numbers in the grid
    for i in range(15):
        #choose random numbers
        row = random.randrange(15)
        col = random.randrange(15)
        num = random.randrange(1,16)
        while(not CheckValid(Grid,row,col,num) or Grid[row][col] != 0): #if taken or not valid reroll
            row = random.randrange(15)
            col = random.randrange(15)
            num = random.randrange(1,16)
        Grid[row][col]= num;
        
    Printgrid(Grid)

def Printgrid(Grid):
    TableTB = "|--------------------------------|"
    TableMD = "|----------+----------+----------|"
    print(TableTB)
    for x in range(15):
        for y in range(15):
            if ((x == 5 or x == 10) and y == 0):
                print(TableMD)
            if (y == 0 or y == 5 or y== 10):
                print("|", end=" ")
            print(" " + str(Grid[x][y]), end=" ")
            if (y == 10):
                print("|")
    print(TableTB)
#     |-----------------------------|
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     |---------+---------+---------|
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     |---------+---------+---------|
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     |-----------------------------|
    
def CheckValid(Grid,row,col,num):
    #check if in row
    valid = True
    #check row and collumn
    for x in range(15):
        if (Grid[x][col] == num):
            valid = False
    for y in range(15):
        if (Grid[row][y] == num):
            valid = False
    rowsection = row // 5
    colsection = col // 5
    for x in range(15):
        for y in range(15):
            #check if section is valid
            if(Grid[rowsection*3 + x][colsection*3 + y] == num):
                valid = False
    return valid

MakeSudoku()
