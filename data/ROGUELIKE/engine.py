import os
import random
import operator
import database_items
import database_npc
import util

def remove_player_from_board(board, player):
    x, y = player['position']
    board[x][y] = '.'

def move_player_to(player, future_x, future_y):
    player['position'] = (future_x, future_y)

def can_move_player_to(board, player, future_x, future_y):
    x, y = player['position']
    scenographic_icons = database_items.scenographic_database.keys()
    
    if future_x not in range(len(board)) or future_y not in range(len(board[x])):
        return False
    elif board[future_x][future_y] in scenographic_icons:
        return False
    elif is_occupied_by_npc(board, future_x, future_y):
        return False
    return True

def create_item_on_board(board, item, x, y):
    board[x][y] = item['icon']
    
def put_item_into_the_inv(player, item):
    if 'value' in item:
        value = item['value']
    else:
        value = 1
    
    if item['name'] not in player['inventory']: 
        player['inventory'][item['name']] = value
    else:
        player['inventory'][item['name']] += value
    
def player_has_item(player, item):
    return item['name'] in player['inventory']

def create_npc_on_board(board, npc, x, y):
    board[x][y] = npc['icon']

def define_npc(player, npc):

    if npc['type'] == 'foe':
        pass
    elif npc['type'] == 'quest':
        pass
    elif npc['type'] == 'shop_npc':
        pass

def is_occupied_by_npc(board, x, y):
    try:
        return board[x][y] in database_npc.npc_database.keys()
    except IndexError:
        return False

def attack(attacker, defender):
    damage = attacker['str'] - defender['def']    
    if defender['def'] >= attacker['str']:
        damage = 0

    if damage > defender['hp']:
        damage = defender['hp']

    defender['hp'] -= damage
    
def fight_is_over(defender):
    return defender['hp'] == 0

def player_vs_npc(player, npc, future_x, future_y):
    attack(player, npc)
    if fight_is_over(npc):
        print('You have won this fight. The legend grows... ')
        remove_npc_from_board(npc, player, future_x, future_y)
        
    attack(npc, player)
    if fight_is_over(player):
        print('You lost... and have become a tasty snack for wolves...')
    

def remove_npc_from_board(npc, player, future_x, future_y):
    move_player_to(player, future_x, future_y)
    player['inventory']['fuertillons'] += npc['value'] 

def choose_weapon_to_use(player, weapon):
    if weapon['str'] > player['gear']['sword']['str']:
        player['str'] -= player['gear']['sword']['str']
        player['str'] += weapon['str']
        player['gear']['sword'] = weapon

def choose_shield_to_use(player, shield):
    if shield['def'] > player['gear']['shield']['def']:
        player['def'] -= player['gear']['shield']['def']
        player['def'] += shield['def']
        player['gear']['shield'] = shield

def use_item_from_inventory(player, item_name):
    if item_name in player['inventory']:
        icon = '\u001b[31mH\u001b[0m' #TO DO HP POT
        item = database_items.item_database[icon]   
        # update player stats
        # deduct item from inv
def take_quest_from_npc(player, npc, item):
    pass

def move_npc_toward_player(player, npc, future_x, future_y):
    pass

def move_boss(player, boss, future_x, future_y):
    pass

def idle_hp_regeneration(player, future_x, future_y):
    x, y = player['position']
    if future_x != x or future_y != y:
        if player['hp'] == 0:
            player['hp'] == 0
        elif player['hp'] < 998:
            player['hp'] += 2
        elif player['hp'] in range(999, 1001):
            player['hp'] = 1000
        
