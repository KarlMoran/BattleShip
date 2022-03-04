import random 

# Player & Computer Map variables
PLAYER_MAP = [[" "] * 8 for i in range(8)]
COMPUTER_MAP = [[" "] * 8 for i in range(8)]
PLAYER_GUESS_MAP = [[" "] * 8 for i in range(8)]
COMPUTER_GUESS_MAP = [[" "] * 8 for i in range(8)]

# Assigns letters to numbers that can be used for ship placements
LETTERS_TO_NUMBERS = {
    'A':0,
    'B':1,
    'C':2,
    'D':3,
    'E':4,
    'F':5,
    'G':6,
    'H':7,
}