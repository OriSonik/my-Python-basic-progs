a = int(input('Podaj liczbe a: '))
b = int(input('Podaj liczbe b: '))
input_string = input('Podaj elementy listy oddzielajac je spacjami: ')
values_list = input_string.split()
print(' ')
print(' ')




                                                                                #MINIMUM z 2 liczb a i b
                                                                                #nasze liczby zostały podane na początku przez użytkownika
def min(a, b):
    if a < b:
        return a
    elif a > b:
        return b
    else:
        return a
print(f'Mniejsza wartoscia z podanych a oraz b jest: {min(a, b)}')






                                                                                #MAXIMUM z dowolnej podanej listy liczb
                                                                                #masza lista została już podana przez użytkownika na początku

def max(values_list):
    max_i = values_list[0]
    for i in values_list:
        if i > max_i:
            max_i = i
    return max_i  
print(f'Najwieksza wartoscia wprowadzona na liste jest {max(values_list)}')

                                   



                                   
                                                                                #DŁUGOŚĆ LISTY (ilość elementów)
                                                                                #nasza lista została już podana przez użytkownika na początku

def len(values_list):
    list_length = 0
    for i in values_list:
        list_length += 1
       

    return list_length

print('Twoja lista sklada sie z ' + str(len(values_list)) + ' elementow')







                                                                                #MNOZENIE wartosci a i b przy uzyciu dodawania wielokrotnego liczby a
                                                                                #liczba a oraz jej wielokrotność o wartości b zostały podane na początku przez użytkownika

suma_a = 0
if b >= 0:
    myrange = range(b)
else:
    myrange = range(-b)

for x in myrange:
    if b >= 0:
        suma_a += a
    else:
        suma_a -= a
print(f'Wynik mnożenia a i b to: {suma_a}')





                                                                                #POTEGOWANIE z 2 podanych liczb a i b
                                                                                #podstawa a oraz jej wykładnik b zostały podane na początku przez użytkownika
# =============== DZIAŁA TYLKO DLA WYKŁADNIKA b >= 0 ===============                       =============== DZIAŁA TYLKO DLA WYKŁADNIKA b >= 0 ===============
def pow(a, b):
    
    akt_b = 0
    c = 1
    while akt_b < b: #czyli gdy podane b > 0
        c = c * a
        akt_b += 1
    
    return c

print(f'Wynik potegowania a^b to: {pow(a, b)}')
# =============== DZIAŁA TYLKO DLA WYKŁADNIKA b >= 0 ===============                       =============== DZIAŁA TYLKO DLA WYKŁADNIKA b >= 0 =============== 








                                                                                #DZIELENIE 2 podanych liczb a i b
                                                                                #dzielna a oraz dzielnik b zostały podane na początku przez użytkownika  

# D O    W Y M Y S L E N I A

# c = a / b
# def div(a, b):
#     return c
# print(f'Wynik dzielenia liczb to: {div(a, b)}')