Fizz_i = 0
Buzz_i = 0
FizzBuzz_i = 0

for x in range(0, 101):
    if x %3 == 0 and x %5 == 0:  # if x %15 == 0:
        print('Fizz Buzz')
        FizzBuzz_i += 1
    elif x % 3 == 0:
        print('Fizz')
        Fizz_i += 1
    elif x % 5 == 0:
        print('Buzz')
        Buzz_i += 1
    else:
        print(x)



print('Koniec FizzBuzzowania, ogarnij sie')
