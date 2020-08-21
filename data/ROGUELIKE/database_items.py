import random

teleportation_orb = {'name': 'teleportation_orb', 'type': 'tp', 'icon': '\u001b[35m#\u001b[0m'}
small_hp_potion = {'name': 'small_hp_potion', 'type': 'potion', 'icon': '\u001b[31mh\u001b[0m', 'hp': 100}
hp_potion = {'name': 'hp_potion', 'type': 'potion', 'icon': '\u001b[31mH\u001b[0m', 'hp': 200}
sword = {'name': 'sword', 'type': 'sword', 'icon': '\u001b[33mi\u001b[0m', 'str': 10}
shield = {'name': 'shield', 'type': 'shield', 'icon': '\u001b[33m)\u001b[0m', 'def': 10}
sword_of_the_mists = {'name': 'sword_of_the_mists', 'type': 'sword', 'icon': '\u001b[33m/\u001b[0m', 'str': 50}
sword_of_the_forgotten_hollows = {'name': 'sword_of_the_forgotten_hollows', 'type': 'sword', 'icon': '\u001b[33m|\u001b[0m', 'str': 150}
sword_of_the_weeping_sacred_willow = {'name': 'sword_of_the_weeping_sacred_willow', 'type': 'sword', 'icon': '\u001b[33m!\u001b[0m', 'str': 250}
philosopher_s_ice = {'name': 'philosopher_s_ice', 'type': 'upgrade', 'icon': '\u001b[34m^\u001b[0m', 'def': 20}
orchidean_absorber = {'name': 'orchidean_absorber', 'type': 'shield', 'icon': '\u001b[34mo\u001b[0m', 'def': 50}
dragonscale_plate = {'name': 'dragonscale_plate', 'type': 'shield', 'icon': '\u001b[34mO\u001b[0m', 'def': 150}
fuertillons = {'name': 'fuertillons', 'icon': '\u001b[33m$\u001b[0m', 'type': 'currency', 'value': random.randint(25,250)}

tree = {'name': 'tree', 'icon': '\u001b[42m\u001b[30mT\u001b[0m'}
tree2 = {'name': 'tree2', 'icon': '\u001b[42m\u001b[30mY\u001b[0m'}
water = {'name': 'water', 'icon': '\u001b[44m\u001b[30m~\u001b[0m'}
wall = {'name': 'bridge', 'icon': '\u001b[41m=\u001b[0m'}

item_database = {
    '\u001b[33m)\u001b[0m': shield, '\u001b[33mi\u001b[0m': sword,
    '\u001b[35m#\u001b[0m': teleportation_orb, '\u001b[31mh\u001b[0m': small_hp_potion,
    '\u001b[31mH\u001b[0m': hp_potion, '\u001b[33mi\u001b[0m': 'sword', '\u001b[33m/\u001b[0m': sword_of_the_mists, 
    '\u001b[33m|\u001b[0m': sword_of_the_forgotten_hollows, '\u001b[33m!\u001b[0m': sword_of_the_weeping_sacred_willow,
    '\u001b[34m^\u001b[0m': philosopher_s_ice, '\u001b[33m$\u001b[0m': fuertillons,
    '\u001b[34mo\u001b[0m': orchidean_absorber, '\u001b[34mO\u001b[0m': dragonscale_plate,
 }

scenographic_database = {
    '\u001b[42m\u001b[30mT\u001b[0m': tree, '\u001b[42m\u001b[30mY\u001b[0m': tree2, 
    '\u001b[44m\u001b[30m~\u001b[0m': water, '\u001b[41m=\u001b[0m': wall,
}
