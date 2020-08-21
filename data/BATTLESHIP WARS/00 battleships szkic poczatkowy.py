CELL_TYPES = []
SHIP_TYPES = [GALACTICA, ARCHERON, VALKYRIE, CHIRON] = 5, 4, 3, 2
SHIP_SIZES = {GALACTICA: 5, ARCHERON: 4, VALKYRIE: 3, CHIRON: 2}
SHIP_NAMES = {GALACTICA: 'Galactica', ARCHERON: 'Archeron', VALKYRIE: 'Valkyrie', CHIRON: 'Chiron'}  

  # generates a battlefield of a desired size -----------------------------------------------------------------------
def generate_board(board_size):
    generated_board = [['.']*board_size for x in range(board_size)]
    return generated_board

  # draws a battlefield with row/column names on it ------------------------------------------------------------------
def draw_board(board): 
    print('  ', end = '')
    for col in range(len(board)):
        print(col + 1, end = ' ')
    print('')    
    
    for ind, row in enumerate(board):
        print(chr(ind + 65), end = ' ')  # int into aplha convert chr(+65) to name rows
        for cell in row:
            print(cell, end = ' ')
        print('')

  # converts user coordinates [alpha,num] (one cell) to logic pair of coords [num,num] --------------------------------
def get_coords(user_coords):
    split_list = user_coords[:1], user_coords[1:]
    first_coord = ord(split_list[0]) - 65                   # TO DO: support upper/lowercase etc. 
    second_coord = int(split_list[1]) - 1

    return [first_coord, second_coord]                      # TO DO: user_coords = input ('Podaj koordy: ')
                                                            
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
            board[beg_x][y] = 'X'
            
    if beg_y == end_y:  # if in the same col
        if end_x < beg_x:
            end_x, beg_x = beg_x, end_x
        for x in range(beg_x, end_x+1): 
            board[x][beg_y] = 'X'
        
    return board

  # deploys ships declared to be put to fight -------------------------------------------------------------------------
def ships_deploy(user_board, ship_types):
    for ship_type in ship_types:
        try:
            coords_from_player = input(f'Provide coordinates for your {SHIP_NAMES[ship_type]} ({SHIP_SIZES[ship_type]}) ship, commander (e.g. A3-A6): ')       
            ship = get_ship_coords(coords_from_player)
            validate_ship(user_board, ship, ship_type)
            place_ship(user_board, ship)
            
            draw_board(user_board)
        except IndexError:
            print('Our ship has just disappeared in outer space, please deploy another one, commander: ')

  # validates the ship declaration ----------- or does not ------------------------------------------------------------
def validate_ship(board, ship, ship_type):

    ship_begin, ship_end = ship
    beg_x, beg_y = ship_begin
    end_x, end_y = ship_end                       # TO DO: if ships stick to each other - don't deploy
    size = len(board)
        
    if beg_x != end_x and beg_y != end_y:                                            # if diagonally put - don't deploy
        print('The ship needs to be deployed in a straight row or column, commander.')

    if beg_x > size or beg_y > size or end_x > size or end_y > size:                  # if out of bounds - don't deploy
        print('The ship needs to be fully deployed in this dimension, commander.')
    
    if abs(beg_x - end_x) + 1 != SHIP_SIZES[ship_type] and abs(beg_y - end_y) + 1 != SHIP_SIZES[ship_type]:  # if other length               
        print('The ship needs one more measuring before deployment. Try again...')                           #  - don't deploy
   
    for board[x][y] != ship[x][y]:       # żeby się      nie stykały............................... !!!!!!!!!!!!!!!!!!!!!!!!!!
        if ship_begin = board[x]+1, board[y]:
                    break;
        elif ship_begin = board[x]+1, board[y]-1:
                    break;
        elif ship_begin = board[x]+1, board[y]+1:
                    break;
        elif ship_begin = board[x], board[y]:
                    break;
        elif ship_begin = board[x], board[y]-1:
                    break;
        elif ship_begin = board[x], board[y]+1:
                    break;
        elif ship_begin = board[x]-1, board[y]:
                    break;
        elif ship_begin = board[x]-1, board[y]-1:
                    break;
        elif ship_begin = board[x]-1, board[y]+1:
                    break;
        
    
  # define the board size and tell what area the player chose for battle placement ------------------------------------
  # determine what quantity of which ship types will the player be asked to place on board ----------------------------
n = int(input('Define the star battle area size (5-10 units): '))
while not n in range(5,11):  
    n = int(input('Choose a valid value, commander: '))
if n == 5:
    print('You chose a sky assault local area, the battle begins:')
    player_ships = [VALKYRIE, CHIRON, CHIRON, CHIRON]
elif n == 6:
    print('You chose a moon invasion area, the battle begins:')
    player_ships = [VALKYRIE, VALKYRIE, CHIRON, CHIRON, CHIRON]
elif n == 7:
    print('You chose a planet takeover area, the battle begins:')
    player_ships = [GALACTICA, VALKYRIE, VALKYRIE, CHIRON, CHIRON, CHIRON]
elif n == 8:
    print('You chose a star system war area, the battle begins:')
    player_ships = [GALACTICA, ARCHERON, VALKYRIE, VALKYRIE, CHIRON, CHIRON, CHIRON]
elif n == 9:
    print('You chose a galactic mission area, the battle begins:')
    player_ships = [GALACTICA, ARCHERON, ARCHERON, VALKYRIE, VALKYRIE, VALKYRIE, CHIRON, CHIRON]
elif n == 10:
    print('You chose a dimensional rift area, the battle begins:')
    player_ships = [GALACTICA, ARCHERON, ARCHERON, VALKYRIE, VALKYRIE, VALKYRIE, CHIRON, CHIRON, CHIRON]   
  # execute the board display -----------------------------------------------------------------------------------------     
if n in range(5,11):
    board = generate_board(n)
    draw_board(board)



ships_deploy(board, player_ships)