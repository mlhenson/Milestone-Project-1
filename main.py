# Milestone Project 1 for 2021 Complete Python Bootcamp
# Tic-tac-toe game for two human players
# Board should be printed every time a player makes a move
# Accept input of player position then place a symbol on the board
# Use the numpad to match numbers to a grid
import random


# Functions
# Clear the board
def clear_board():
    print('\n' * 20)


# Prints the current board state
def printboard():
    print(f" {boardplaces[6]} | {boardplaces[7]} | {boardplaces[8]}\n"
          f"-- + - + --\n"
          f" {boardplaces[3]} | {boardplaces[4]} | {boardplaces[5]}\n"
          f"-- + - + --\n"
          f" {boardplaces[0]} | {boardplaces[1]} | {boardplaces[2]}\n")


# Asks the user for a number on where they want to place their piece
def user_choice(valid_numbers):
    # Initial value
    choice = 'nope'
    while not choice.isdigit():
        choice = input(f"Okay {playernames[currentplayer]}, you're up! Pick a number to place your piece (1-9): ")

        # Check if user input is number
        if not choice.isdigit():
            print("It seems you haven't entered a number.")

        # If user input is a number, check if it's in range
        # Sets choice back to string if not in range
        elif int(choice) not in valid_numbers and int(choice) in range(1, 9):
            print("That spot is already taken, try another!")
            choice = 'invalid'
        elif int(choice) not in valid_numbers:
            print("That number isn't valid, try another one!")
            choice = 'invalid'
        else:
            return int(choice)


# Randomizes the starting player
def random_player():
    randint = int(random.randrange(1, 100))
    if randint <= 50:
        outputint = 0
    else:
        outputint = 1
    # print(f"DEBUG_RANDINT: {randint}")
    return outputint


# Asks the first player whether they want to be X or O and writes them to a list, returns the list to be used
def set_player_symbol(currentplayer):
    symbolchoices = ["X", "O"]
    symbols_set = False
    symbols = ["A", "B"]
    while not symbols_set:
        # print(f"DEBUG_SYMBOLS: {symbols}")
        symbols[currentplayer] = input(f"Okay {playernames[currentplayer]}, would you rather be X or O? ")
        if symbols[currentplayer] not in symbolchoices:
            print("Please choose X or O")
            # print(f"DEBUG_SYMBOLS: {symbols}")
        elif symbols[0] == "X":
            symbols[1] = "O"
            symbols_set = True
        elif symbols[0] == "O":
            symbols[1] = "X"
            symbols_set = True
        elif symbols[1] == "X":
            symbols[0] = "O"
            symbols_set = True
        elif symbols[1] == "O":
            symbols[0] = "X"
            symbols_set = True
    # print(f"DEBUG_SYMBOLS: {symbols}")
    return symbols


# Write the symbol of the current player to the position it gets passed (position validity is checked in user_choice)
def place_piece(position):
    boardplaces[position - 1] = playersymbol[currentplayer]


# Checks all possible combinations to see if a player has won
# Returns a tuple, the first is if the game is over and the second is if it's a cat's game
# This returned tuple can then be writen to it's own variable then applied to variables controlling the main while loop
def win_check(boardlist):
    # Top Horizontal
    if boardlist[6] == playersymbol[currentplayer] and boardlist[7] == playersymbol[currentplayer] \
            and boardlist[8] == playersymbol[currentplayer]:
        return True, False

    # Mid Horizontal
    elif boardlist[3] == playersymbol[currentplayer] and boardlist[4] == playersymbol[currentplayer] \
            and boardlist[5] == playersymbol[currentplayer]:
        return True, False

    # Bot Horizontal
    elif boardlist[0] == playersymbol[currentplayer] and boardlist[1] == playersymbol[currentplayer] \
            and boardlist[2] == playersymbol[currentplayer]:
        return True, False

    # Left Vertical
    elif boardlist[6] == playersymbol[currentplayer] and boardlist[3] == playersymbol[currentplayer] \
            and boardlist[0] == playersymbol[currentplayer]:
        return True, False

    # Mid Vertical
    elif boardlist[7] == playersymbol[currentplayer] and boardlist[4] == playersymbol[currentplayer] \
            and boardlist[1] == playersymbol[currentplayer]:
        return True, False

    # Right Vertical
    elif boardlist[8] == playersymbol[currentplayer] and boardlist[5] == playersymbol[currentplayer] \
            and boardlist[2] == playersymbol[currentplayer]:
        return True, False

    # Top Left Diagonal
    elif boardlist[6] == playersymbol[currentplayer] and boardlist[4] == playersymbol[currentplayer] \
            and boardlist[2] == playersymbol[currentplayer]:
        return True, False

    # Top Right Diagonal
    elif boardlist[0] == playersymbol[currentplayer] and boardlist[4] == playersymbol[currentplayer] \
            and boardlist[8] == playersymbol[currentplayer]:
        return True, False

    # Cat's game check
    # Go through the board state and output any strings into a new list
    content_type = []
    for item in boardlist:
        if type(item) == str:
            content_type += item
    # If the newly output list is all strings it'll match the input and no valid integer locations will remain
    if boardlist == content_type:
        # print("DEBUG: CATS GAME")
        return True, True

    return False, False


# Play again?
def play_again():
    symbolchoices = ["Y", "N"]
    play_again_set = False
    while not play_again_set:
        play_again_response = input(f"Would you like to play again? (Y or N) ")
        if play_again_response not in symbolchoices:
            print("Please choose Y or N")
            play_again_response = "invalid"
        elif play_again_response == "Y":
            return True
        elif play_again_response == "N":
            return False


# Variables
boardplaces = list(range(1, 10))
gameover = False
draw_game = False
playernames = ["Player 1", "Player 2"]
gamereset = False

# Game Start
print("Welcome to Tic-tac-toe!")
playernames[0] = input("Player 1, what is your name? ")
playernames[1] = input("Player 2, what is your name? ")
print("Let's see who is gonna go first...")
currentplayer = random_player()
print(f"Great! Looks like {playernames[currentplayer]} is starting us off!")
playersymbol = set_player_symbol(currentplayer)
clear_board()

# Main gameplay loop
while not gameover:
    # Display the board
    printboard()

    # Place the piece based off of what the user picks, using a list to determine if the place is taken already or not
    place_piece(user_choice(boardplaces))

    # Win check and cat's game check
    win_check_output = win_check(boardplaces)
    gameover = win_check_output[0]
    draw_game = win_check_output[1]
    # gameover = win_check(boardplaces)

    # Clear the board and congrats the player who won and break the loop
    if gameover:
        clear_board()
        printboard()
        if not draw_game:
            print(f"Congratulations {playernames[currentplayer]}, you've won!")
        elif draw_game:
            print("Cat's game!")

    # If the game isn't over at this point, switch the player
    if currentplayer == 0:
        currentplayer = 1
    else:
        currentplayer = 0

    # Prompt the user if they'd like to restart if the game ended during play
    while gameover:
        gamereset = play_again()
        if gamereset is False:
            break
        else:
            boardplaces = list(range(1, 10))
            draw_game = False
            gamereset = False
            print("Switching up who goes first this time...")
            currentplayer = random_player()
            print(f"Great! Looks like {playernames[currentplayer]} is starting us off!")
            gameover = False
            continue

    clear_board()
