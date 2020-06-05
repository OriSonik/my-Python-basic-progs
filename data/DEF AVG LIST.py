input_string = input('Podaj elementy listy oddzielajac je spacjami: ')
values_list = input_string.split()

list_len = len(values_list)
sum = 0
for x in values_list:
    sum += int(x)
avg = sum / list_len
print(f'Srednia wartosc wyrazenia na liscie wynosi {avg}')