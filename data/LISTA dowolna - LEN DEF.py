input_string = input('Podaj elementy listy oddzielajac je spacjami: ')
values_list = input_string.split()
def len(values_list):
    list_length = 0
    for i in values_list:
        list_length += 1
       

    return list_length

print('Twoja lista sklada sie z ' + str(len(values_list)) + ' elementow')