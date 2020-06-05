a = int(input('Podaj liczbe a: '))
b = int(input('Podaj liczbe b: '))

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