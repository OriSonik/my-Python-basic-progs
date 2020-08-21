import database_player

def how_is_the_hp(player):
    s = '[    |    |    |    |     ]'
    if player['hp'] <= 0: 
        colour = '\u001b[46m'
        s = '[Your Hero Has Lost R.I.P.]'    
    elif player['hp'] <= 50: 
        colour = '\u001b[45m'
        s = '[!   |    |    |    |     ]'
    elif player['hp'] <= 100: 
        colour = '\u001b[45m'
        s = '[!!  |    |    |    |     ]'
    elif player['hp'] <= 400:
        colour = '\u001b[41m'
    elif player['hp'] <= 800:
        colour = '\u001b[43m'
    else:
        colour = '\u001b[42m'
    reset_index = int(player['hp']/40)+1
    s = s[:reset_index] + '\u001b[0m' + s[reset_index:]
    s = s[:1] + colour + s[1:]
    print(s, player['hp']/10,'%')

def board_level_info(board_list, current_board):
    for k, v in board_list.items():
        if current_board == v:
            return k

def encode_location(board_list, current_board, x, y):
    return f'{board_level_info(board_list, current_board)}-{x}-{y}'

def help():
    print('\n__ ITEMS: ____________\n\u001b[35m#\u001b[0m : teleportation orb\n\u001b[31mh, H\u001b[0m : hp potions\n\u001b[33m/ | !\u001b[0m : weapons\n\u001b[34m^ o O\u001b[0m : defensives\n\u001b[33m$\u001b[0m : fuertillon coins\n\n__ STRUCTURES: _______\n... : bridges & ground\n1 2 3 : portals\n\u001b[41m====\u001b[0m : walls\n\u001b[42m\u001b[30mTY\u001b[0m : trees\n\u001b[44m\u001b[30m~\u001b[0m : water\n4 - cave\n\n__ NPCs: _____________\n\u001b[7mQ\u001b[0m : quest NPC\n\u001b[1m\u001b[93mW\u001b[0m : howler\n\u001b[1m\u001b[93mA\u001b[0m : thug\n\u001b[1m\u001b[93mM\u001b[0m : mist guard\n\u001b[1m\u001b[92mW\u001b[0m : shadowtail\n\u001b[1m\u001b[92mA\u001b[0m : tough thug\n\u001b[1m\u001b[92mM\u001b[0m : mist knight\n\u001b[1m\u001b[33mW\u001b[0m : nowherewolf\n\u001b[1m\u001b[33mA\u001b[0m : steroidruid\n\u001b[1m\u001b[33mM\u001b[0m : mist spectre\n\u001b[1m\u001b[91mV\u001b[0m : boss Pika-chew-bacca\n\n')

def how_is_the_npc_hp(npc):
        
    s = '[    |    |    |    |     ]'
    if npc['hp'] <= 0: 
        colour = '\u001b[46m'
        s = '[   V  I  C  T  O  R  Y   ]'    
    elif npc['hp'] <= int(0.05 * npc['max_hp']): 
        colour = '\u001b[45m'
        s = '[!   |    |    |    |     ]'
    elif npc['hp'] <= int(0.10 * npc['max_hp']): 
        colour = '\u001b[45m'
        s = '[!!  |    |    |    |     ]'
    elif npc['hp'] <= int(0.4 * npc['max_hp']):
        colour = '\u001b[41m'
    elif npc['hp'] <= int(0.8 * npc['max_hp']):
        colour = '\u001b[43m'
    else:
        colour = '\u001b[42m'
    i = npc['hp']/25
    try:
        reset_index = int(npc['hp']/i)+1
    except ZeroDivisionError:
        reset_index = 1
        
    s = s[:reset_index] + '\u001b[0m' + s[reset_index:]
    s = s[:1] + colour + s[1:]
    print(s, int(100 * (npc['hp']) / (npc['max_hp'])),'%')

def print_player_stats(player):
    print(f"PLAYER'S STRENGTH: {player['str']}, DEFENSE: {player['def']}")