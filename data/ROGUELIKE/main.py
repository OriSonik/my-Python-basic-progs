import engine
import util
import ui
import database_boards
import database_player
import database_items
import database_npc
import extras
import os
import random


 
def main():
    util.clear_screen()
    
    player = database_player.create_player()
    
    board_list = database_boards.create_boards()
    current_board = board_list['1']
    npc_dictionary = {}
    
    is_running = True
    npc = None
    while is_running:

        x, y = player['position']
        future_x = x
        future_y = y   

        print('Current Howling Forest Region: ',extras.board_level_info(board_list, current_board))
        extras.how_is_the_hp(player)
        extras.print_player_stats(player)
        if npc:
            extras.how_is_the_npc_hp(npc)
            if engine.fight_is_over:
                npc = None
        database_player.put_player_on_board(current_board, player)
        ui.display_board(current_board)

        key = util.key_pressed()
        
        if key == 'q':
            is_running = False
        elif key == 'w':
            future_x = x - 1
        elif key == 's':
            future_x = x + 1
        elif key == 'a':
            future_y = y - 1
        elif key == 'd':
            future_y = y + 1
        elif key == 'i':
            print(player['inventory'])
            util.press_any_key()
        elif key == 'h':
            extras.help()
            util.press_any_key()
        elif key == 'k':
            item = database_items.small_hp_potion
            engine.use_item_from_inventory(player, item)
        elif key == 'l':
            item = database_items.small_hp_potion
            engine.use_item_from_inventory(player, item)
        else:
            pass
        engine.remove_player_from_board(current_board, player)            
        database_player
# moves the player to the next/previous board(s) if has the teleportation orb // put items to inv
        if engine.can_move_player_to(current_board, player, future_x, future_y):
            engine.idle_hp_regeneration(player, future_x, future_y)
            if database_boards.is_cell_exit(current_board, future_x, future_y):
                if engine.player_has_item(player, database_items.teleportation_orb):
                    for key in board_list:                                          
                        if current_board[future_x][future_y] == key:                
                            current_board = board_list[key]
                            break                         
                    if future_y == 0:
                        player['position'] = future_x, future_y + database_boards.BOARD_WIDTH - 2
                    else:
                        player['position'] = future_x, future_y - database_boards.BOARD_WIDTH + 2
                    database_player.put_player_on_board(current_board,player)
                else:
                    print('You need to find the teleportation orb first... (#)')
                    util.press_any_key()
            else: 
                engine.move_player_to(player, future_x, future_y)
                if current_board[future_x][future_y] in database_items.item_database:           
                    item = database_items.item_database[current_board[future_x][future_y]]
                    if item['type'] == 'sword':
                        engine.choose_weapon_to_use(player, item)
                    elif item['type'] == 'shield':
                        engine.choose_shield_to_use(player, item)
                    elif item['type'] == 'upgrade':
                        engine.add_upgrade_to_stats(player, item)
                    else:
                        engine.put_item_into_the_inv(player, item)
                    

        elif engine.is_occupied_by_npc(current_board, future_x, future_y):
            npc_key = extras.encode_location(board_list, current_board, future_x, future_y)
            if npc_key in npc_dictionary:
                npc = npc_dictionary[npc_key]
            else:
                npc = database_npc.npc_database[current_board[future_x][future_y]].copy()
                npc_dictionary[npc_key] = npc
            extras.how_is_the_npc_hp(npc)
            engine.player_vs_npc(player, npc, future_x, future_y)   
            if player['hp'] == 0:
                is_running = False            
        util.clear_screen()

if __name__ == '__main__':
    main()
