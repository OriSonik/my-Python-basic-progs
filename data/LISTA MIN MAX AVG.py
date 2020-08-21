#MIN
numbers = [-5, -20003, 0, -9, 12, 99, 105, -43]
l = numbers[0]
for y in numbers:
    if y < l:
        l = y
print(l)

#MAX
numbers = [-5, -20003, 0, -9, 12, 99, 105, -43]
l = numbers[0]
for y in numbers:
    if y > l:
        l = y
print(l)

#AVG
numbers = [5,6,3,5]
l = len(numbers)
sum = 0
for x in numbers:
    sum += x
avg = sum / l
print(avg)
