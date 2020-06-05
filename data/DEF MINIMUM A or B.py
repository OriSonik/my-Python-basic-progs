a = int(input('Podaj liczbe a: '))
b = int(input('Podaj liczbe b: '))

def min(a, b):
    if a < b:
        return a
    elif a > b:
        return b
    else:
        return a
print(f'Mniejsza wartoscia z podanych a oraz b jest: {min(a, b)}')