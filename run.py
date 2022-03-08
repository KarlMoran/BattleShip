import random
import time

# Player & Computer Map variables
PLAYER_MAP = [[" "] * 8 for i in range(8)]
COMPUTER_MAP = [[" "] * 8 for i in range(8)]
PLAYER_GUESS_MAP = [[" "] * 8 for i in range(8)]
COMPUTER_GUESS_MAP = [[" "] * 8 for i in range(8)]

# Assigns letters to numbers that can be used for ship placements
LETTERS_TO_NUMBERS = {
    'A': 0,
    'B': 1,
    'C': 2, 
    'D': 3, 
    'E': 4, 
    'F': 5, 
    'G': 6,
    'H': 7
    }

SPACER = "≠" * 50

# The SHIP_SIZE list contains the size of each ship on the map
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

    # Welcome Message
    print("\nWelcome To Battleships!\n")
    print("THE MAP IS A GRID OF 8x8 WITH FIVE SHIPS TO SINK")
    print("DESTROYER - GREYHOUND - DICKY - SUBMARINE - ESCORT")
    print("EACH PLAYER HAS 17 LIVES, \
THE FIRST TO STRIKE 17 BLOWS TO THE ENEMYS SHIPS WINS\n")
    time.sleep(5)
    print(SPACER) 

    # Instructions
    print("\u001b[31mINSTRUCTIONS:\u001b[0m \n")
    print("THE FIRST PLAYER TO GET A HIT COUNT OF 17 HITS DESTROYING ALL ENEMY \
SHIPS WINS")
    print("THE AIM OF THE GAME IS TO DESTROY THE AI \
ENEMY BY DESTROYING ALL THEIR SHIPS")
    print("BEFORE THEY DESTROY YOURS. THE THING IS WELL \
BOTH OF YOU CANT SEE WHERE TO")
    print("SHOOT... BUT THAT SHOULDNT BE MUCH OF A PROBLEM.")
    print("THE RULES ARE AS FOLLOWS: \n")
    print("SHIPS: \n")
    print("ESCORT - SIZE OF 2 ON THE BOARD\n")
    print("SUBMARINE - SIZE OF 3 ON THE BOARD\n")
    print("DICKY - SIZE OF 3 ON THE BOARD\n")
    print("GREYHOUND - SIZE OF 4 ON THE BOARD\n")
    print("DESTROYER - SIZE OF 5 ON THE BOARD\n")
   
    # Instructions - KEYS
    print("KEYS: \n")
    print("∆ IS A SHIP")
    print("- IS A MISS")
    print("X IS A HIT/SUNK SHIP")
    time.sleep(5)
    print(SPACER)

def print_map(map):
    """
    The print_map function prints out the battleship map
    """
    # Header for the game 
    print( "  A B C D E F G H")
    # Spacer between header and map
    print( "  •-•-•-•-•-•-•-•")
    row_number = 1
    for row in map:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def place_ship(map):
    """
    The place ship function loops throught the lengths of the ships and then
    loops until the ship fits and dosent overlap any ships on the map,
    then places the ship.
    """
    #loop between length of ships
    for ship_size in SHIP_SIZE:
        #loop around until ship fit in map
        while True:
            if map == COMPUTER_MAP:
                orientation, row, column = random.choice(["H", "V"]), \
                    random.randint(0, 7), random.randint(0, 7)
                if ship_size_check(ship_size, row, column, orientation):
                    #check for overlapping ship
                    if not ship_overlap(map, row, column, orientation, ship_size):
                        #placing ships
                        if orientation == "H":
                            for i in range(column, column + ship_size):
                                map[row][i] = "∆"
                        else:
                            for i in range(row, row + ship_size):
                                map[i][column] = "∆"
                        break
            else:
                place_ship = True
                print('Place the ship with a length of ' + str(ship_size))
                row, column, orientation = user_input(place_ship)
                if ship_size_check(ship_size, row, column, orientation):
                    #Check for overlapping ships
                    if ship_overlap(map, row, column, orientation, ship_size) == False:
                          #Placing ships
                        if orientation == "H":
                            for i in range(column, column + ship_size):
                                map[row][i] = "∆"
                        else:
                            for i in range(row, row + ship_size):
                                map[i][column] = "∆"
                        print_map(PLAYER_MAP)
                        break

def ship_size_check(SHIP_SIZE, row, column, orientation):
    """
    The hip_size_check checks if the ships inputted fit on the map
    """
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
    """
    The ship_overlap function checks if inputted ships overlap any existing
    ships already on the map
    """
    if orientation == "H":
        for i in range(column, column + ship_size):
            if map[row][i] == "∆":
                return True
    else:
        for i in range(row, row + ship_size):
            if map[i][column] == "∆":
                return True
    return False


def user_input(place_ship):
    """
    The user_input function takes input from the user when they want to place 
    their ships as well as guessing the computers ships on the map
    """
    if place_ship == True:
        while True:
            try:
                orientation = input("PLease enter orientation H or V : \n").upper()
                if orientation == "H" or orientation == "V":
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid orientaion (H or V)")
        while True:
            try:
                row = input("Enter the row of the ship 1-8: \n")
                if row in '12345678':
                    row = int(row) - 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid letter between 1-8")
        while True:
            try:
                column = input("Enter the column of the ship A-H: \n").upper()
                if column not in 'ABCDEFGH':
                    print("Please enter a valid letter between A-H")
                else:
                    column = LETTERS_TO_NUMBERS[column]
                    break
            except KeyError:
                print("Please enter a valid letter between A-H")
        return row, column, orientation
    else:
        while True:
            try:
                row = input("Enter the row of the ship 1-8: \n")
                if row in '12345678':
                    row = int(row) - 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid letter between 1-8")
        while True:
            try:
                column = input("Enter the column of the ship A-H: \n").upper()
                if column not in 'ABCDEFGH':
                    print("Please enter a valid letter between A-H")
                else:
                    column = LETTERS_TO_NUMBERS[column]
                    break
            except KeyError:
                print("Please enter a valid letter between A-H")
        return row, column

def hit_count(map):
    """
    The hit_count function counts the number of hits each map (Player,
    Computer) has taken
    """
    count = 0
    for row in map:
        for column in row:
            if column == "X":
                count += 1
    return count

# User/Computer turn on game (don't need orientation)
def turn(map):
    """
    The turn function goes through the users and computers turns
    """
    if map == PLAYER_GUESS_MAP:
        row, column = user_input(PLAYER_GUESS_MAP)
        if map[row][column] == "-":
            turn(map)
        elif map[row][column] == "X":
            turn(map)
        elif COMPUTER_MAP[row][column] == "∆":
            map[row][column] = "X"
            print("WE HIT THEM, GREAT SHOT")
        else:
            map[row][column] = "-"
            print("WE MISSED")
    else:
        row, column = random.randint(0, 7), random.randint(0, 7)
        if map[row][column] == "-":
            turn(map)
        elif map[row][column] == "X":
            turn(map)
        elif PLAYER_GUESS_MAP[row][column] == "∆":
            map[row][column] = "X"
            print("WE ARE HIT, FIRE BACK!")
            print("COMPUTERS MAP \n")
        else:
            map[row][column] = "-"
            print("THE COMPUTER MISSED,\n")
            print("COMPUTERS MAP \n")

def start_game():
    """
    Start game 
    """
    start_key = input("Press the letter P to start game: \n").upper()
    while start_key !="P":
        start_key = input("Press the letter P to start game: \n").upper()
        print(SPACER)
        # Computer places ships
        place_ship(COMPUTER_MAP)
        # Computer board displayed
        #print_map(COMPUTER_MAP)
        print_map(PLAYER_MAP)
        # Player places ships
        place_ship(PLAYER_MAP)
        
        while True:
            while True:
                print('Guess a battleship location on the map')
                print_map(PLAYER_GUESS_MAP)
                turn(PLAYER_GUESS_MAP)
                break
            if hit_count(PLAYER_GUESS_MAP) == 17:
                print("Congratulations You have sunk all the battleships, You win!!!")
                break
            while True:
                turn(COMPUTER_GUESS_MAP)
                break
            print_map(COMPUTER_GUESS_MAP)
            if hit_count(COMPUTER_GUESS_MAP) == 17:
                print("Sorry, The computer has sunk all your ships. You lose")
                break

def play_again():
    """
    Asks the player if they want to play again or leave 
    """
    print("WOULD YOU LIKE TO PLAY AGAIN?, CAPTAIN \n")
    answer = input("ENTER Y OR N: \n").upper()
    print(' ')
    while True:
        if answer == "Y":
            print(SPACER)
            time.sleep(3)
            welcome_message()
        elif answer == "N":
            print(' ')
            print('GOODBYE!, SEE YOU SOON NEXT TIME')
            print(' ')
            print(SPACER)
            return False
            welcome_message()
        else:
            print(' ')
            print('PLEASE ENTER Y OR N')
            answer = input('ENTER Y OR N: \n').upper()

if __name__ == "__main__":
    welcome_message()
    start_game()
    play_again()