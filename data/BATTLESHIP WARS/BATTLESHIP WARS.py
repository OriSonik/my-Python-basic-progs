import itertools
import os
os.system('cls')

H = '\u001b[17m\u001b[31mH\u001b[37;1m\u001b[40m'   # REDonDarkBL                    #  end background \u001b[40m
X = '\u001b[47m\u001b[32mX\u001b[37;1m\u001b[40m'   # GREENonWHITE                   #  end fontcolour \u001b[37;1m
o = '\u001b[44;1m\u001b[30mo\u001b[37;1m\u001b[40m' # BLACKonBrBLUE

CELL_TYPES = [X, o, H, '.'] # taken, missed, hit, empty
SHIP_TYPES = [GALACTICA, ARCHERON, VALKYRIE, CHIRON] = 5, 4, 3, 2
SHIP_SIZES = {GALACTICA: 5, ARCHERON: 4, VALKYRIE: 3, CHIRON: 2}
SHIP_NAMES = {GALACTICA: 'Galactica', ARCHERON: 'Archeron', VALKYRIE: 'Valkyrie', CHIRON: 'Chiron'}  

# generates a battlefield of a desired size -----------------------------------------------------------------------
def generate_board(board_size):
    generated_board = [['\u001b[44;1m\u001b[34;1m.\u001b[37;1m\u001b[40m']*board_size for x in range(board_size)]
    return generated_board

# draws a battlefield with row/column names on it ------------------------------------------------------------------
def draw_board(board, player_name): 
    print('Player ' + player_name)
    print('  ', end = '')
    for col in range(len(board)):
        print(col + 1, end = ' ')
    print('')     
    for ind, row in enumerate(board):
        print(chr(ind + 65), end = ' ')                                 # int into aplha convert chr(+65) to name rows
        for cell in row:
            print(cell, end = ' ')
        print('')

# draws 2 boards aside each other -----------------------------------------------------------------------------------
def draw_two_boards(board_1, board_2, player_1, player_2):
    print(player_1 + ' '*(len(board_1)*2+4-len(player_1)) + player_2)
    
    print('  ', end = '')
    for col in range(len(board_1)):
        print(col + 1, end = ' ')

    print('    ', end = '')
    for col in range(len(board_2)):
        print(col + 1, end = ' ')
    print('')     

    for ind, row in enumerate(board_1):
        print(chr(ind + 65), end = ' ')                                 # int into aplha convert chr(+65) to name rows
        for cell in board_1[ind]:
            print(cell, end = ' ')
        print('  ' + chr(ind + 65), end = ' ')
        for cell in board_2[ind]:
            print(cell, end = ' ')
        print('')

# converts user coordinates [alpha,num] (one cell) to logic pair of coords [num,num] --------------------------------
def get_coords(user_coords):
    split_list = user_coords[:1], user_coords[1:]               # take up to 1st arg from list, take next after 1st arg
    first_coord = ord(split_list[0]) - 65                                  # change alpha into num [ord / chr function]
    second_coord = int(split_list[1]) - 1

    return [first_coord, second_coord]                      
                                                            
# converts beginning-end whole ship coordinates to 2 pairs of x,y ---------------------------------------------------
def get_ship_coords(user_coords):
    ship_begin, ship_end = user_coords.split('-')
    final_coords_begin = get_coords(ship_begin)
    final_coords_end = get_coords(ship_end)
    return [final_coords_begin, final_coords_end]

# adds a defined whole ship to the battlefield ----------------------------------------------------------------------
def place_ship(board, ship):

    ship_begin, ship_end = ship
    beg_x, beg_y = ship_begin
    end_x, end_y = ship_end
  
    if beg_x == end_x:  # if in the same row
        if end_y < beg_y:
            end_y, beg_y = beg_y, end_y
        for y in range(beg_y, end_y+1):
            board[beg_x][y] = X
            
    if beg_y == end_y:  # if in the same col
        if end_x < beg_x:
            end_x, beg_x = beg_x, end_x
        for x in range(beg_x, end_x+1): 
            board[x][beg_y] = X
        
    return board

# deploys ships declared to be put to fight -------------------------------------------------------------------------
def ships_deploy(user_board, ship_types, player_name):
    for ship_type in ship_types:
        validating = True
        while validating:
            i = SHIP_SIZES[ship_type]
            try:
                coords_from_player = input(f'Provide coordinates for your {SHIP_NAMES[ship_type]} ({SHIP_SIZES[ship_type]}) ship, commander (e.g. A1-A{i}): ').upper()      
                ship = get_ship_coords(coords_from_player)                
                if validate_ship(user_board, ship, ship_type):
                    validating = False
            except ValueError:
                print('Please, for once, put the bottle down and deploy the ship like a real commander')
            except IndexError:
                print('Our ship has just disappeared in outer space, please deploy another one, commander: ')
        place_ship(user_board, ship)
        draw_board(user_board, player_name)
        
# validates the ship declaration ----------- or does not ------------------------------------------------------------
def validate_ship(board, ship, ship_type):

    ship_begin, ship_end = ship
    beg_x, beg_y = ship_begin
    end_x, end_y = ship_end                       
    size = len(board)
    

    if beg_x != end_x and beg_y != end_y:                                                     # if diagonally put - don't deploy
        print('The ship needs to be deployed in a straight row or column, commander.')
        return False
    elif beg_x >= size or beg_y >= size or end_x >= size or end_y >= size:                     # if out of bounds - don't deploy
        print('The ship needs to be fully deployed in this dimension, commander.')
        return False
    elif beg_x < 0 or beg_y < 0 or end_x < 0 or end_y < 0:                                   # if out of bounds 2 - don't deploy
        print('The ship needs to be fully deployed in this dimension, commander.')
        return False
    elif abs(beg_x - end_x) + 1 != SHIP_SIZES[ship_type] and abs(beg_y - end_y) + 1 != SHIP_SIZES[ship_type]:  # if other length               
        print('The ship needs one more measuring before deployment. Try again...')                             #  - don't deploy
        return False
    elif is_ship_touching_another(board, ship):                                           # if ships are touching - don't deploy   
        print('The ship got damaged crashing into another one. Deploy a new ship...')
        return False

    return True

# checks all the surrounding cells around the placing cell -----------------------------------------------------------
def is_valid_placement(board, x, y):
    if is_taken(board, x+1, y):
        return False         
    elif is_taken(board, x+1, y-1):
        return False        
    elif is_taken(board, x+1, y+1):
        return False     
    elif is_taken(board, x, y):
        return False      
    elif is_taken(board, x, y-1):
        return False            
    elif is_taken(board, x, y+1):
        return False            
    elif is_taken(board, x-1, y):
        return False        
    elif is_taken(board, x-1, y-1):
        return False    
    elif is_taken(board, x-1, y+1):
        return False
    else:
        return True

# is_valid_placement upgrade for out of bounds check and for already occupied -------- addon for previous f ---------- 
def is_taken(board, x, y):
    return 0 <= x < len(board) and 0 <= y < len(board) and board[x][y] == X

# determines if the ship would be touching another one ---------------------------------------------------------------
def is_ship_touching_another(board, ship):
    ship_begin, ship_end = ship
    beg_x, beg_y = ship_begin
    end_x, end_y = ship_end     

    if beg_x == end_x:  # if in the same row
        if end_y < beg_y:
            end_y, beg_y = beg_y, end_y
        for y in range(beg_y, end_y+1):
            if is_valid_placement(board, beg_x, y) == False:
                return True
            
    if beg_y == end_y:  # if in the same col
        if end_x < beg_x:
            end_x, beg_x = beg_x, end_x
        for x in range(beg_x, end_x+1): 
            if is_valid_placement(board, x, beg_y) == False:
                return True
    
    return False

# define shooting method  
def shoot(target_board, deployed_board, x, y):
    if deployed_board[x][y] == X:
        target_board[x][y] = H
    else:
        target_board[x][y] = '\u001b[35mo\u001b[37;1m'
    

# converts a board (list of lists) into a single list - merged ------------ for a WIN check if Xs = Hs ---------------
def make_board_list(board):
    return list(itertools.chain.from_iterable(board))

# change all players' boards into single lists to make them comparable 
def count_on_board(board, elem):
    board_list = make_board_list(board)
    return board_list.count(elem)

# define the board size and tell what area the player chose for battle placement -------------------------------------
# determine what quantity of which ship types will the player be asked to place on board -----------------------------
# ask players for names to identify whose turn it is in the battle ----- color brighten ------------------------------
print("\u001b[37;1mCOMMANDERS' NAMES:")
player_1 = input('Enter your name, fleet commander 1: ')
player_2 = input('Enter your name, fleet commander 2: ')
players = [player_1, player_2]
print(' ')
print('BATTLE AREA:')
n = int(input('Define the star battle area size (5-10 units): '))

# comment the board size chosen and determine which ships to deploy for that size ------------------------------------
while not n in range(5,11):
    if n < 5:  
        n = int(input('Choose a bigger area, commander: '))
    if n > 10:
        n = int(input('Choose a smaller area, commander: '))
if n == 5:
    print('You chose a sky assault local area, the battle begins:')
    player_1_ships = [VALKYRIE, CHIRON, CHIRON]
elif n == 6:
    print('You chose a moon invasion area, the battle begins:')
    player_1_ships = [VALKYRIE, VALKYRIE, CHIRON, CHIRON]
elif n == 7:
    print('You chose a planet takeover area, the battle begins:')
    player_1_ships = [GALACTICA, VALKYRIE, VALKYRIE, CHIRON, CHIRON]
elif n == 8:
    print('You chose a star system war area, the battle begins:')
    player_1_ships = [GALACTICA, ARCHERON, VALKYRIE, VALKYRIE, CHIRON, CHIRON]
elif n == 9:
    print('You chose a galactic mission area, the battle begins:')
    player_1_ships = [GALACTICA, ARCHERON, ARCHERON, VALKYRIE, VALKYRIE, CHIRON, CHIRON]
elif n == 10:
    print('You chose a dimensional rift area, the battle begins:')
    player_1_ships = [GALACTICA, ARCHERON, ARCHERON, VALKYRIE, VALKYRIE, VALKYRIE, CHIRON, CHIRON]  
player_2_ships = player_1_ships 
  
# execute the boards and initiate ship deployment -------------------------------------------------------------------     
board_1 = generate_board(n)
board_2 = generate_board(n)
board_1_t = generate_board(n)
board_2_t = generate_board(n)

print(' ')
print(f" \u001b[36;1m============== COMMANDER {player_1}'S TURN FOR STAR SHIPS DEPLOYMENT ==============\u001b[37;1m ")
ships_deploy(board_1, player_1_ships, player_1)

os.system('cls')
print(' ')
print(f" \u001b[36;1m============== COMMANDER {player_2}'S TURN FOR STAR SHIPS DEPLOYMENT ==============\u001b[37;1m")
ships_deploy(board_2, player_2_ships, player_2)

os.system('cls') 
# shooting phase for 2 players ------------ determine when the game ends --------------------------------------------
while True:
    try:
        shot = input(f'Aim at a target cell, commander {player_1} (e.g. C1): ').upper()
        x, y = get_coords(shot)
        shoot(board_1_t, board_2, x, y)
        draw_two_boards(board_1_t, board_2_t, player_1, player_2)
        print('')
    except ValueError:
        print('The missile hit an innocent alien cargo ship, far away...')
    except IndexError:
        print:('Told you to put that bottle away')
    
    if count_on_board(board_2, X) == count_on_board(board_1_t, H):
        print(f'CONGRATULATIONS! {player_1} wins! CONGRATULATIONS!')
        break
    
    try:
        shot = input(f'Aim at a target cell, commander {player_2} (e.g. C2): ').upper()
        x, y = get_coords(shot)
        shoot(board_2_t, board_1, x, y)
        draw_two_boards(board_1_t, board_2_t, player_1, player_2)
        print('')
    except ValueError:
        print('The missile hit an innocent alien schoolbus ship, far away...')
    except IndexError:
        print:('Told you to put that bottle away')

    if count_on_board(board_1, X) == count_on_board(board_2_t, H):
        print(f'CONGRATULATIONS! {player_2} wins! CONGRATULATIONS!')
        break


    

