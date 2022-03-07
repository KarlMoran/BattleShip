import random

# Player & Computer Map variables
PLAYER_MAP = [[" "] * 8 for i in range(8)]
COMPUTER_MAP = [[" "] * 8 for i in range(8)]
PLAYER_GUESS_MAP = [[" "] * 8 for i in range(8)]
COMPUTER_GUESS_MAP = [[" "] * 8 for i in range(8)]

# Assigns letters to numbers that can be used for ship placements
LETTERS_TO_NUMBERS = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

# The SHIP_SIZE list contains the size of each ship on the board
SHIP_SIZE = [2, 3, 3, 4, 5]

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
    # Header for the game 
    print( "  A B C D E F G H")
    # Spacer between header and map
    print( "  •-•-•-•-•-•-•-•")
    row_number = 1
    for row in map:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def place_ships(map):
    #loop between length of ships
    for ship_size in SHIP_SIZE:
        #loop around until ship fit in map
        while True:
            if map == COMPUTER_MAP:
                orientation, row, column = random.choice("H", "V"), random.randint(0, 7), random.randint(0, 7)
                if ship_size_check(ship_size, row, column, orientation):
                    #check for overlapping ships 
                    if ship_overlap(map, row, column, orientation, ship_size) == False:
                        #placing ships
                        if orientation == "H":
                            for i in range(column, column + ship_size):
                                board[row][i] = "∆"
                        else:
                            for i in range(row, row + ship_size):
                                board[i][column] = "∆"
                        break
            else:
                place_ship = True
                print('Place the ship with a length of ' + str(ship_size))
                row, column, orientation = user_input(place_ship)
                if ship_size_check(SHIP_SIZE, row, column, orientation):
                    #check for overlapping ships 
                    if ship_overlap(map, row, column, orientation, ship_size) == False:
                        #placing ships
                        if orientation == "H":
                            for i in range(column, column + ship_size):
                                board[row][i] = "∆"
                        else:
                            for i in range(row, row + ship_size):
                                board[i][column] = "∆"
                        print_map(PLAYER_MAP)
                        break



def ship_size_check(SHIP_SIZE, row, column, orientation):
    if orientation == "H":
        if column + SHIP_SIZE > 8:
            return False
        else:
            return True
    else:
        if row + SHIP_SIZE > 8:
            return False
        else:
            return True

def ship_overlap(map, row, column, orientation, ship_size):
    if orientation == "H":
        for i in range(column, column + ship_size):
            #check to see if ship is overlap
            if map [row][i] == "∆":
                return True
    else:
        for i in range(row, row + ship_size):
            if map [row][i] == "∆":
                return True
    return False


def user_input():
    pass

def hit_count():
    pass

def turn(map):
    pass

#while True: