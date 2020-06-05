a = int(input('Podaj liczbe a: '))
b = int(input('Podaj liczbe b: '))

def pow(a, b):
    c = 1
    while b >= 0:
        c = c * a
        b -= 1

    return c

print(f'Wynikiem potegowania jest: {pow(a, b)}')