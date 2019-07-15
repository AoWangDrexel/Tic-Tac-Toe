"""
Description: A modified version of the Tic-Tac-Toe game months ago, but with other 
principles in Python, such as dictionaries, helper functions, loops, and great ASCII art

Author: Ao Wang
Completed: 07/15/19
"""

# creating a dictionary, keys: position of the symbols, values: Os or Xs
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# printing the tictactoe board as a function
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# method to check each column of the board for a winner according to the position, L-Left, M-Middle, R-Right
def colCheck(pos):
    colCounter = 0
    colX = 0
    colO = 0
    # loops through the dict. keys and only checks if equal the position
    for i in theBoard.keys():
        if pos in i:
            if theBoard[i] == "X":
                colX += 1
            if theBoard[i] == "O":
                colO += 1
            colCounter += 1

        if colCounter == 3 and (colX == 3 or colO == 3):
            if colX == 3:
                print("Player X won!")
            else: 
                print("Player O won!")
            return True  
    return False
    
def winChecker(theBoard):
    countO = 0
    countX = 0
    rowCounter = 0
    
    # goes through all the rows of the board
    for i in theBoard.keys(): # accessing each of the keys of the dictionary
        
        # winning results in either countX or countO increasing to 3, which is a strike
        if theBoard[i] == "X":
            countX += 1
        if theBoard[i] == "O":
            countO += 1
        rowCounter += 1
        
        if rowCounter == 3 and (countX == 3 or countO == 3):
            if countX == 3:
                print("Player X won!")
            else: 
                print("Player O won!")
            return True
        # once a row is completed, it results back to 0 and continues to +1 to the next row
        if rowCounter == 3:
            rowCounter = 0
            countX = 0
            countO = 0
      
        # checks each column if winner, luckily resets the colX, colO, and colChecker because they are local variables
        # to the function
    if colCheck("L") or colCheck("M") or colCheck("R") :
        return True
    
    # checks the diagonals for victory
    if (theBoard["top-L"] == theBoard["mid-M"] == theBoard["low-R"] == "X") or (theBoard["top-R"] == \
        theBoard["mid-M"] == theBoard["low-L"] == "X"):                                                               
        print("Player X win!")
        return True
        
    if (theBoard["top-L"] == theBoard["mid-M"] == theBoard["low-R"] == "O") or (theBoard["top-R"] == \
        theBoard["mid-M"] == theBoard["low-L"] == "O"):
        print("Player O win!")
        return True
                   
    return False

# function to start game
def playGame():
    turn = "X"
    count = 0
    # game ends when winChecker returns true, meaning a player won or when there is a tie when all moves are used
    while(not winChecker(theBoard) and count != 9):
        printBoard(theBoard)     
        move = input("Turn for " + turn + " . Move on which space? (Exit Press 0): ")
        
        # ends game if move input is 0
        if move.isnumeric() and int(move) == 0:
            print("Game ended!")
            break
        
        # if the input move is not in the dictionary keys, repeat until so
        while(not move in theBoard.keys()):
            print("No such command")
            move = input("Turn for " + turn + " . Move on which space? (Exit Press 0): ")
            
            # includes two break statements to exit out completely
            if move.isnumeric() and int(move) == 0:
                print("Game ended!")
                break
        if move.isnumeric() and int(move) == 0:
            break
        
        # if spot in board is empty, fill with symbol, otherwise pick another spot
        if theBoard[move] == " ":
            theBoard[move] = turn
        else:
            print("Sorry, there was a mark already")
            # catches exception if move is not part of dictionary keys
            try:
                while(theBoard[move] != " "):
                    move = input("Turn for " + turn + " . Move on which space? (Exit Press 0): ")
                    
                    if move.isnumeric() and int(move) == 0:
                        print("Game ended!")
                        break
                if move.isnumeric() and int(move) == 0:
                    break         
            except KeyError:
                print("Sorry, no such command")
            theBoard[move] = turn
        
        # switching turns from X to O and so forth
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
        
        # counts the number of symbols on the board
        count += 1
        
        # tie checker
        if count == 9 and not winChecker(theBoard):
            print("It was a tie!")
            printBoard(theBoard)
        
        # win checker
        if winChecker(theBoard):
            printBoard(theBoard) 
            break
            
# awesome ascii art as the starting screen
print("""
 __      __         .__                                       __            
/  \    /  \  ____  |  |    ____    ____    _____    ____   _/  |_   ____   
\   \/\/   /_/ __ \ |  |  _/ ___\  /  _ \  /     \ _/ __ \  \   __\ /  _ \  
 \        / \  ___/ |  |__\  \___ (  <_> )|  Y Y  \\  ___/   |  |  (  <_> ) 
  \__/\  /   \___  >|____/ \___  > \____/ |__|_|  / \___  >  |__|   \____/  
       \/        \/            \/               \/      \/                  

        888   d8b        888                   888                    
        888   Y8P        888                   888                    
        888              888                   888                    
        888888888 .d8888b888888 8888b.  .d8888b888888 .d88b.  .d88b.  
        888   888d88P"   888       "88bd88P"   888   d88""88bd8P  Y8b 
        888   888888     888   .d888888888     888   888  88888888888 
        Y88b. 888Y88b.   Y88b. 888  888Y88b.   Y88b. Y88..88PY8b.     
         "Y888888 "Y8888P "Y888"Y888888 "Y8888P "Y888 "Y88P"  "Y8888  
                                                              
""")
playGame()
