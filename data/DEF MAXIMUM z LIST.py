input_string = input('Podaj elementy listy oddzielajac je spacjami: ')
values_list = input_string.split()

def max(values_list):
    max_i = values_list[0]
    for i in values_list:
        if i > max_i:
            max_i = i
    return max_i  
print(f'Najwieksze jest {max(values_list)}')