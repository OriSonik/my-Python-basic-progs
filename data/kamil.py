lista_miast = ['warszawa', 'praga', 'berlin']
wylosowany_indeks = 1

def get_podkreslniki(wyraz):
    return len(wyraz) * ' _ '

miasto_x = (lista_miast[wylosowany_indeks]) 
print(get_podkreslniki(miasto_x))

litera_podana_przez_uzytkownika = input('Podaj litere: ')

i = 0
for litera in miasto_x:
    i += 1
    if litera == litera_podana_przez_uzytkownika:
        
        
        print(litera + ' ' + str(i))

def odslon_odgadniete_litery(get_podkreslniki, litera_podana_przez_uzytkownika, miasto_x):
    czesciowo_odgadniety_wyraz = ''
    for litera_podana_przez_uzytkownika in miasto_x:
        if litera_podana_przez_uzytkownika == litera:
            czesciowo_odgadniety_wyraz = czesciowo_odgadniety_wyraz + litera_podana_przez_uzytkownika
        else:
            czesciowo_odgadniety_wyraz = czesciowo_odgadniety_wyraz + ' _ '
    return czesciowo_odgadniety_wyraz
       
print(czesciowo_odgadniety_wyraz)