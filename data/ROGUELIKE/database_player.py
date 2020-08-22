import extras
import database_items

PLAYER_ICON = '\u001b[47m\u001b[35m@\u001b[0m'
PLAYER_START_X = 3
PLAYER_START_Y = 3


def create_player():
    return {
        'icon': PLAYER_ICON, 
        'position': (PLAYER_START_X, PLAYER_START_Y), 
        'inventory': {
            'fuertillons': 50,
            'small_hp_potion': 2,    
        },
        'gear': {
            'sword': database_items.sword,
            'shield': database_items.shield,
        },
        'hp': 1000,
        'str' : 80 + database_items.sword['str'],
        'def': 20 + database_items.shield['def'],
    }

def put_player_on_board(board, player):
    x, y = player['position']
    board[x][y] = player['icon']