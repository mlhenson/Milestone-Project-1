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
# Want to figure out a cleaner way to do this
def win_check(boardlist):
    # Top Horizontal
    if boardlist[6] == playersymbol[currentplayer] and boardlist[7] == playersymbol[currentplayer] \
            and boardlist[8] == playersymbol[currentplayer]:
        return True

    # Mid Horizontal
    elif boardlist[3] == playersymbol[currentplayer] and boardlist[4] == playersymbol[currentplayer] \
            and boardlist[5] == playersymbol[currentplayer]:
        return True

    # Bot Horizontal
    elif boardlist[0] == playersymbol[currentplayer] and boardlist[1] == playersymbol[currentplayer] \
            and boardlist[2] == playersymbol[currentplayer]:
        return True

    # Left Vertical
    elif boardlist[6] == playersymbol[currentplayer] and boardlist[3] == playersymbol[currentplayer] \
            and boardlist[0] == playersymbol[currentplayer]:
        return True

    # Mid Vertical
    elif boardlist[7] == playersymbol[currentplayer] and boardlist[4] == playersymbol[currentplayer] \
            and boardlist[1] == playersymbol[currentplayer]:
        return True

    # Right Vertical
    elif boardlist[8] == playersymbol[currentplayer] and boardlist[5] == playersymbol[currentplayer] \
            and boardlist[2] == playersymbol[currentplayer]:
        return True

    # Top Left Diagonal
    elif boardlist[6] == playersymbol[currentplayer] and boardlist[4] == playersymbol[currentplayer] \
            and boardlist[2] == playersymbol[currentplayer]:
        return True

    # Top Right Diagonal
    elif boardlist[0] == playersymbol[currentplayer] and boardlist[4] == playersymbol[currentplayer] \
            and boardlist[8] == playersymbol[currentplayer]:
        return True
    return False


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


# # Cats Game checker
# def cats_game(boardlist):
#     # Check if everything is filled
#     for item in range(0, 8):
#         slots_filled = 0
#         if type(boardlist[item]) == type(1):
#             print(type(boardlist[item]))
#         else:
#             slots_filled += 1
#             print(slots_filled)
#         if slots_filled == 9:
#             return True


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
    gameover = win_check(boardplaces)
    # draw_game = cats_game(boardplaces)

    # Clear the board and congrats the player who won and break the loop
    if gameover:
        clear_board()
        printboard()
        if not draw_game:
            print(f"Congratulations {playernames[currentplayer]}, you've won!")
        elif draw_game:
            print("Cat's game!")

    # If it made it this far, no one's won so switch the player and clear the board
    if currentplayer == 0:
        currentplayer = 1
    else:
        currentplayer = 0
    clear_board()

    # Restart game
    while gameover:
        gamereset = play_again()
        print(gamereset)
        if gamereset is False:
            clear_board()
            break
        else:
            clear_board()
            boardplaces = list(range(1, 10))
            draw_game = False
            gamereset = False
            print("Let's see who is gonna go first this time!")
            currentplayer = random_player()
            print(f"Great! Looks like {playernames[currentplayer]} is starting us off!")
            gameover = False
            continue

