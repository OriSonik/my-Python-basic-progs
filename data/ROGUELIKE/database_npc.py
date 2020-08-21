import random

howler = {'name': 'howler', 'type': 'foe', 'icon': '\u001b[1m\u001b[93mW\u001b[0m', 'def': 0, 'str': 50, 'hp': 250, 'max_hp': 250, 'value': random.randint(25,51)}
thug = {'name': 'thug', 'type': 'foe', 'icon': '\u001b[1m\u001b[93mA\u001b[0m', 'def': 0, 'str': 70, 'hp': 300, 'max_hp': 300, 'value': random.randint(25,71)}
mist_guard = {'name': 'guard', 'type': 'foe', 'icon': '\u001b[1m\u001b[93mM\u001b[0m', 'def': 0, 'str': 90, 'hp': 450, 'max_hp': 450, 'value': random.randint(25,91)}

shadowtail = {'name': 'shadowtail', 'type': 'foe', 'icon': '\u001b[1m\u001b[92mW\u001b[0m', 'def': 0, 'str': 70, 'hp': 350, 'max_hp': 350, 'value': random.randint(25,71)}
tough_thug = {'name': 'tough_thug', 'type': 'foe', 'icon': '\u001b[1m\u001b[92mA\u001b[0m', 'def': 0, 'str': 90, 'hp': 450, 'max_hp': 450, 'value': random.randint(25,91)}
mist_knight = {'name': 'mist_knight', 'type': 'foe', 'icon': '\u001b[1m\u001b[92mM\u001b[0m', 'def': 0, 'str': 110, 'hp': 550, 'max_hp': 550, 'value': random.randint(25,111)}

nowherewolf = {'name': 'nowherewolf', 'type': 'foe', 'icon':'\u001b[1m\u001b[33mW\u001b[0m', 'def': 0, 'str': 90, 'hp': 450, 'max_hp': 450, 'value': random.randint(25,91)}
steroidruid = {'name': 'steroidruid', 'type': 'foe', 'icon':'\u001b[1m\u001b[33mA\u001b[0m', 'def': 0, 'str': 110, 'hp': 550, 'max_hp': 550, 'value': random.randint(25,111)}
mist_spectre = {'name': 'mist_spectre', 'type': 'foe', 'icon':'\u001b[1m\u001b[33mM\u001b[0m', 'def': 0, 'str': 130, 'hp': 700, 'max_hp': 700, 'value': random.randint(25,131)}
boss = {'name': 'The_Pika-chew-bacca', 'type': 'foe', 'icon':'\u001b[1m\u001b[91mV\u001b[0m', 'def': 150, 'str': 250, 'hp': 1500, 'max_hp': 1500, 'value': random.randint(25,251)}

def boss_char(boss, board):
    pass

mysterious_spirit = {'name': 'mysterious_spirit', 'type': 'quest_npc', 'icon': '\u001b[7mQ\u001b[0m', 'value': random.randint(101,501)}
shadowborn_merchant = {'name': 'shadowborn_merchant', 'type': 'shop_npc', 'icon': '\u001b[7mS\u001b[0m', 'inventory': {}}
npc_database = {
    '\u001b[1m\u001b[93mW\u001b[0m': howler, '\u001b[1m\u001b[93mA\u001b[0m': thug, '\u001b[1m\u001b[93mM\u001b[0m': mist_guard,
    '\u001b[1m\u001b[92mW\u001b[0m': shadowtail, '\u001b[1m\u001b[92mA\u001b[0m': tough_thug, '\u001b[1m\u001b[92mM\u001b[0m': mist_knight,
    '\u001b[1m\u001b[33mW\u001b[0m': nowherewolf, '\u001b[1m\u001b[33mA\u001b[0m': steroidruid, '\u001b[1m\u001b[33mM\u001b[0m': mist_spectre,
    '\u001b[1m\u001b[91mV\u001b[0m': boss, '\u001b[7mQ\u001b[0m': mysterious_spirit, '\u001b[7mS\u001b[0m': shadowborn_merchant,
}

