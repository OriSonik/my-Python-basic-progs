def add(a, b):
    c = a + b
    return c


def sub(a, b):
    c = a - b
    return c


def mul(a, b):
    c = a * b
    return c


def div(a, b):
    c = a / b
    return c


def pow(a, b):
    c = a ** b
    return c


def calculate(a, b, sign):
    if sign == '+':
        return add(a, b)
    elif sign == '-':
        return sub(a, b)
    elif sign == '*':
        return mul(a, b)
    elif sign == '/':
        return div(a, b)
    elif sign == '**':
        return pow(a, b)
    else:
        return 0


def read_number(text):
    a = int(input(text))
    return a

def print_calculation(a, b, sign, result):
    print (f"Your calculation is: {a} {sign} {b} = {result}" )

def main():
    a = read_number("Specify the first number: ")
    sign = input("Specify the calculation typing it's sign: ")
    b = read_number("Specify the second number: ")
    result = calculate(a, b, sign)
    print_calculation(a, b, sign, result)

main()