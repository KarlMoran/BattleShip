import random

# Player & Computer Map variables
PLAYER_MAP = [[" "] * 8 for i in range(8)]
COMPUTER_MAP = [[" "] * 8 for i in range(8)]
PLAYER_GUESS_MAP = [[" "] * 8 for i in range(8)]
COMPUTER_GUESS_MAP = [[" "] * 8 for i in range(8)]

# Assigns letters to numbers that can be used for ship placements
LETTERS_TO_NUMBERS = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

def welcome_message():
    """
    The welcome_message function displays a welcome message
    """
    print("""\
   ___             _       _        _              ___    _         _      _ __  
  | _ )   __ _    | |_    | |_     | |     ___    / __|  | |_      (_)    | '_ \ 
  | _ \  / _` |   |  _|   |  _|    | |    / -_)   \__ \  | ' \     | |    | .__/ 
  |___/  \__,_|   _\__|   _\__|   _|_|_   \___|   |___/  |_||_|   _|_|_   |_|__  
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'      
\
""")

def print_map(map):
    print( "  A B C D E F G H")
    print( "  •-•-•-•-•-•-•-•")
    row_number = 1
    for row in map:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def place_ships(map):
    pass

def ship_size_check():
    pass

def ship_overlap():
    pass

def user_input():
    pass

def hit_count():
    pass

def turn(map):
    pass

#while True: