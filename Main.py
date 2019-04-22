def win_checker(board):
    len_row = len(board)
    len_col = len(board[0])
    
    sum_of_row = 0 
    sum_of_col = 0
    diagonal_left = 0
    diagonal_right = 0
    
    for row in range(0,len_row):
        for col in range(0,len_col):
            sum_of_row += ord(board[row][col])
            sum_of_col += ord(board[col][row])
        if(sum_of_row == 360 or sum_of_row == 333 or sum_of_col == 360 or sum_of_col == 333):
            return True
        else:
            sum_of_row = 0
            sum_of_col = 0
    
    
    diagonal_left = ord(board[0][0]) + ord(board[1][1]) + ord(board[2][2])
    diagonal_right = ord(board[0][2]) + ord(board[1][1]) + ord(board[2][0])
    
    if(diagonal_left == 360 or diagonal_left == 333 or diagonal_right == 360 or diagonal_right == 333):
        return True
    else:
        return False

def place_tic_or_tac(row,col,board,mark):
    if(row<len(board)and col <len(board[0]) and board[row][col]!= "x" and board[row][col]!="o"):
        board[row][col] = mark;
        return True
    return False

board = [["-","-","-"],
         ["-","-","-"],
         ["-","-","-"]]


print("Hello, welcome to the Tic Tac Toe Game!")
first_name = input("Player One (x) : ")
second_name = input("Player Two (o) : ")

row = 0
col = 0
counter = 0
while((not(win_checker(board))) and counter !=9):
    passing = False
    if(counter%2 == 0):
        print("Make your move, "+ first_name)
        while(not passing):
            row = int(input("Row:"))
            col = int(input("Column:"))
            if(place_tic_or_tac(row,col,board,"x")):
                passing = True
            else:
                print("Please try again")
    else:
        print("Make your move, "+ second_name)
        while(not passing):
            row = int(input("Row:"))
            col = int(input("Column:"))
            if(place_tic_or_tac(row,col,board,"o")):
                passing = True
            else:
                print("Please try again")
            
    counter+=1
    print(board[0])
    print(board[1])
    print(board[2])
    
if(counter%2==0):
    print(second_name+ " wins!")
elif(counter == 9):
    print("It's a tie")
else:
    print(first_name + " wins!")
