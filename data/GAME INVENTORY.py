def display_inventory (inventory):
    for k, v in inventory.items():  # zamiana dict na list
        print(f'{k}: {v}')

def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1     
    
def remove_from_inventory(inventory, removed_items):
    for item in removed_items:
        if item in inventory:
            inventory[item] -= 1
            if inventory[item] <= 0:
                del inventory[item]


def print_table(inventory, order = ''):
    
    if order == 'count,asc':
        sorted_items = sorted(inventory.items(), key=lambda x: x[1])
    elif order == 'count,desc':
        sorted_items = sorted(inventory.items(), key=lambda x: x[1], reverse=True)
    else:
        sorted_items = inventory.items()        
    
    max_item_len = max(len(k) for k in inventory) 
    if max_item_len < 9:
        max_item_len = 9
    max_qnt_len = max(len(str(inventory[k])) for k in inventory)
    if max_qnt_len < 5:
        max_qnt_len = 5
    separator = '-' * (max_item_len + max_qnt_len + 3)


    print(separator)
    print(' ' * (max_item_len - 9) + 'item name' + ' | ' + ' ' * (max_qnt_len - 5) + 'count')
    print(separator)
    for k, v in sorted_items:
        k = ' ' * (max_item_len - len(k)) + k
        v = str(v)
        v = ' ' * (max_qnt_len - len(v)) + v
        print(f'{k} | {v}')
    print(separator)   


def import_inventory(inventory, filename="import_inventory.csv"):
    try:
        filename = open(filename).readlines()
        new_string = filename[0]
        new_string = new_string.split(',')
        add_to_inventory(inventory, new_string)
    except FileNotFoundError:
        print(f"File '{filename}' not found!")
  
    

def export_inventory(inventory, filename='export_inventory.csv'):
    try:
        newstring = ''
        for x in inventory:
            newstring += (x + ',') * inventory[x]
        newstring = newstring[:-1]                                        # delete comma after last arg 
        with open(filename, 'w') as myfile:                               # can also be done with "newstring.rstrip(',')" command 
            myfile.write(newstring)
    except PermissionError:
        print(f"You don't have permission creating file '{filename}'!")

if __name__ == '__main__':

    inventory = {'gold coins': 45, 'mithril arrows': 12, 'torches': 6,}
    display_inventory(inventory)
    print('---')
    add_to_inventory(inventory, ['rubies', 'mithril arrows', 'torches', 'axes', 'mithril arrows', 'axes', 'elven longbows'] )
    display_inventory(inventory)
    print('---')
    remove_from_inventory(inventory, ['rubies', 'axes', 'torches', 'axes', 'rubies', 'magic staff', 'torches'])
    display_inventory(inventory)
    print('---')
    print_table(inventory)
    print('---')
    export_inventory(inventory, "export_inventory.csv")
    print('---')
    import_inventory(inventory, "import_inventory.csv")
    print_table(inventory)



