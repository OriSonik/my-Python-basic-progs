a = int(input('Podaj liczbe a: '))
b = int(input('Podaj liczbe b: '))

def pow(a, b):
    
    akt_b = 0
    c = 1
    while akt_b < b: #czyli gdy podane b > 0
        c = c * a
        akt_b += 1
    
    return c

print(f'Wynik potegowania a^b to: {pow(a, b)}')

# DZIAŁA TYLKO DLA WYKŁADNIKA b >= 0
