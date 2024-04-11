board = [
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "]
    ]

first_marker = "X" #determines the marker for player 1
second_marker = "O" #determines the marker for player 2
win = False #win/loss variable - if its true, the game should stop
current_player = "Player One" #determines who needs to play

#This function prints the board.
#Run this function to check it out!
def print_board():
    print(" 1 2 3 4 5 6 7")
    for i in range(len(board)):
        for j in board[i]:
            print(j+"|",end="")
        print("")
print_board()

def player_one():
    global board
    marker = "X"
    ask = int(input("What column would you like to play? "))
    if board[0][ask] != " ":
        print("Play another column")
        insert_piece()
    for i in range(6,0,-1):
        if board[i][ask] != " ":
            continue
        else:
            board[i][ask] = marker
            break
    print_board()
    win_lose()
    player_two()

def player_two():
    global board
    marker = "O"
    ask = int(input("What column would you like to play? "))
    if board[0][ask] != " ":
        print("Play another column")
        insert_piece()
    for i in range(6,0,-1):
        if board[i][ask] != " ":
            continue
        else:
            board[i][ask] = marker
            break
    print_board()
    win_lose()
    player_one()

#def insert_piece():
    #you can use this function to insert the piece onto the board

def win_loss():
    #Create logic to check if someone has won
    #If someone has won, change the win variable to True
    #Make a print state saying who won or lost


#This runs the game... be careful running this (infinite loop)
while win != True:
    if current_player == "Player One":
        player_one()
    if current_player == "Player Two":
        player_two()



    
