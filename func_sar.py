# Definējam dažādās funkcijas
def multiply(a, b):
    return a*b

def power(a, b):
    return a**b

def substract(a, b):
    return a-b

def add(a, b):
    return a+b

def divide(a, b):
    if b != 0:
        return a/b
    else:
        return 'cannot divide by 0'

functions = [multiply, power, substract, add, divide]
# Kā izsaukt visas funkcijas:
a = 10
b = 5
for func in functions:
    print(f'{func.__name__}({a}, {b}) = {func(a, b)}')


# Testēšana, funkciju izsaukšana
print(f'skaitļu 2 un 3 reizinājums ir {multiply(2, 3)}')
print(power(2, 3))
print(substract(2, 3))
print(add(2, 3))
print(divide(2, 0))