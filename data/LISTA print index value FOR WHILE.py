lista = [1,2,5,4,3]

                    # WYPISYWANIE WARTOSCI ELEMENTOW:                           FOR
for el in lista:
    print("Wartosc:", el)

                    #WYNIK:
                    # Wartosc: 1
                    # Wartosc: 2
                    # Wartosc: 5
                    # Wartosc: 4
                    # Wartosc: 3




                    # WYPISYWANIE INDEKSOW Z PRZYPISANYMI WARTOSCIAMI:          FOR
for i in range(len(lista)):
    print("Indeks:", i, ", wartosc:", lista[i])

                    # WYNIK:
                    # Indeks: 0 , wartosc: 1
                    # Indeks: 1 , wartosc: 2
                    # Indeks: 2 , wartosc: 5
                    # Indeks: 3 , wartosc: 4
                    # Indeks: 4 , wartosc: 3



                    # WYPISYWANIE INDEKSOW Z PRZYPISANYMI WARTOSCIAMI:          WHILE
i = 0
while i < len(lista):
    print("Indeks:", i, ", wartosc:", lista[i])
    i += 1

                    # WYNIK:
                    # Indeks: 0 , wartosc: 1
                    # Indeks: 1 , wartosc: 2
                    # Indeks: 2 , wartosc: 5
                    # Indeks: 3 , wartosc: 4
                    # Indeks: 4 , wartosc: 3