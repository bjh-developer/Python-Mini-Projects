#tic tac toe game created by Joon Hao, built in Visual Studio code with Python 3

import time
#intro
print("Welcome to a game of Tic Tac Toe!")
time.sleep(2)
print("First player will be 'x' and second player will be 'o'.")
time.sleep(3)


# ------- Global Variables ------

#game board
board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"]


#if game is still going
game_still_going = True

#who won or tie?
winner = None

#whose turn is it
current_player = "x"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():

    #display initial board
    display_board()

    while game_still_going:

            #handle a single turn of a player
        handle_turn(current_player)

        #check is the game is over
        check_if_game_over()

        #flip to the other player
        flip_player()

    #the game has ended
    if winner == "x" or winner == "o":
        print(winner + " won!")
    elif winner == None:
        print("Tie...")

#handle a single turn of a player
def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position 1 - 9: ")
    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1 - 9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again")

    board[position] = player

    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():

    #set up global variables
    global winner


    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():
    #set up global variables
    global game_still_going
    #check if any row have all the same value
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #if
    if row_1 or row_2 or row_3:
        game_still_going = False
    #return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[1]
    elif row_3:
        return board[2]
    return

def check_columns():
    #set up global variables
    global game_still_going
    #check if any row have all the same value
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    #if
    if column_1 or column_2 or column_3:
        game_still_going = False
    #return the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    #set up global variables
    global game_still_going
    #check if any row have all the same value
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    #if
    if diagonal_1 or diagonal_2:
        game_still_going = False
    #return the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    #global variable we need
    global current_player
    #if current player is x, change to o
    if current_player == "x":
        current_player = "o"
    #if current player is o, change to x
    elif current_player == "o":
        current_player = "x"
    return

play_game()

#board
#display board
#play game
#handle turn
#check win
    #check rows
    #check columns
    #check diagonals
#check tie
#flip player
