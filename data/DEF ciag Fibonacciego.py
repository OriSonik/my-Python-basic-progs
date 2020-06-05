# a(n) = a(n-1) + a(n-2)

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

for n in range(1, 35):
    print(fibonacci(n))
