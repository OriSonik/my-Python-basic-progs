import extras

PLAYER_ICON = '\u001b[47m\u001b[35m@\u001b[0m'
PLAYER_START_X = 3
PLAYER_START_Y = 3


def create_player():
    return {
        'icon': PLAYER_ICON, 
        'position': (PLAYER_START_X, PLAYER_START_Y), 
        'inventory': {
            'fuertillons' : 50,
            'small_hp_potion': 2,
            
        },
        'hp': 1000,
        'str' : 100,
        'def': 20,
    }

def put_player_on_board(board, player):
    x, y = player['position']
    board[x][y] = player['icon']