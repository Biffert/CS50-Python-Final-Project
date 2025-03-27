import sys
import re
import os
import string
from tabulate import tabulate # Library 'tabulate[widechars]' required for emoji support in tables
from random import choice
from pyfiglet import Figlet


os.system("clear")
figlet = Figlet()   # Create header font
figlet.setFont(font="slant")    # Set header font

def main():
    # Print title
    print(figlet.renderText("Mine Finder"))

    # Enter field size
    while True:
        try:
            difficulty = int(input("Choose field size between 5 and 10: "))
            if 5 <= difficulty <= 10:
                break
        except ValueError:
            print("Please enter an integer in the range of 5 to 10. Press Ctrl + C to exit.")
        except KeyboardInterrupt:
            print("\n")
            sys.exit(figlet.renderText("Goodbye!"))

    previous_moves = []
    bomb_location =  choice(string.ascii_lowercase[:difficulty]) + choice("".join(str(i) for i in range(1, difficulty + 1))) # ascii_lowercase[:difficulty] shows the first difficulty number of letters. // "" is the seperator for .join()
    turn = 1
    mine_field = generate_field(difficulty)

    # Loop until all fields cleared or bomb field selected

    while turn != (difficulty*difficulty):
        try:
            os.system("clear")
            print(tabulate(mine_field, headers="keys", tablefmt="double_grid")) # Print mine field with tabulate
            print("Turn:", turn)
            player_move = input("What's your move? ").lower()
            while True:
                if not valid_move(player_move, difficulty, previous_moves):
                    print("Invalid move or field already cleared. Please try again or press Ctrl + C to exit.")
                    player_move = input("What's your move? ").lower()
                elif player_move == bomb_location: # If player_move == bomb_location sys.exit()
                    mine_field = parse_move(player_move, mine_field, bomb_location)
                    os.system("clear")
                    print(tabulate(mine_field, headers="keys", tablefmt="double_grid"))
                    sys.exit(figlet.renderText("Your head a splode!"))
                else:
                    previous_moves.append(player_move) # Store player_move in previous_moves
                    break
            turn += 1
            mine_field = parse_move(player_move, mine_field, bomb_location)
        except KeyboardInterrupt:
            print("\n")
            sys.exit(figlet.renderText("Goodbye!"))

    # Print "You survived!" when all fields have been cleared
    os.system("clear")
    print(tabulate(mine_field, headers="keys", tablefmt="double_grid"))
    sys.exit(figlet.renderText("You survived!"))

def generate_field(difficulty): # Generates mine field in a list of dictionaries
    mine_field = []
    i = 1
    letter = "a"
    while i != difficulty + 1: # Repeat this for number of rows requested by difficulty input
        mine_field_row = {" ": letter} # Generate mine field 'row' as a dictionary
        mine_field_row.update({str(i): "🟩" for i in range(1, difficulty + 1)}) # Add no. of 'columns' based on difficulty input
        mine_field.append(mine_field_row) # Add row to mine_field list.
        i += 1
        letter = chr(ord(letter)+1) # Next letter
    return mine_field

def valid_move(player_move, difficulty, previous_moves): # Check whether user input is a valid field or was part of previous input
    valid_letters = "|".join(chr(97 + i) for i in range(difficulty)) # create list of valid rows (letters) seperated by "|" for RegEx
    valid_numbers = "|".join(str(i) for i in range(1, difficulty + 1)) # create list of valid columns (numbers) seperated by "|" for RegEx
    if not re.search(rf"^({valid_letters})({valid_numbers})$", player_move):
        return False
    elif player_move in previous_moves: # check whether move has been done before
        return False
    else:
        return True

def parse_move(player_move, mine_field, bomb_location): # Process player move

    # Flag locations
    flag_L = bomb_location[0] + str(int(bomb_location[1]) - 1) # Add flag to previous column from bomb
    flag_R = bomb_location[0] + str(int(bomb_location[1]) + 1) # Add flag to next column from bomb
    flag_U = chr(ord(bomb_location[0])-1) + bomb_location[1] # Add flag to previous row from bomb, by choosing previouis letter. ord() convert to ASCII & chr() convert back to alpha
    flag_D = chr(ord(bomb_location[0])+1) + bomb_location[1] # Add flag to next row from bomb

    if player_move == bomb_location:
        for d in mine_field: # Iterate through list mine_field
            if d.get(" ") == player_move[0]: # Get value for " " which returns row a, b, c etc...
                d[player_move[1]] = "💣" # Replace with value
        return mine_field
    elif player_move == flag_L or player_move == flag_R or player_move == flag_U or player_move == flag_D: # Place flag when flag location is entered by user
        for d in mine_field: # Iterate through list mine_field
            if d.get(" ") == player_move[0]: # Get value for " " which returns row a, b, c etc...
                d[player_move[1]] = "🚩" # Replace with value
    else: # Place dirt when grass location is entered by user
        for d in mine_field: # Iterate through list mine_field
            if d.get(" ") == player_move[0]: # Get value for " " which returns row a, b, c etc...
                d[player_move[1]] = "🟫" # Replace with value
    return mine_field

if __name__ == "__main__":
    main()
