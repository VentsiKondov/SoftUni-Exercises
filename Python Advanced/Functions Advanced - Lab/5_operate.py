from functools import \
    reduce


def operate(symbol,*numbers):
    if symbol == '+':
        return reduce(lambda a, b: a + b, numbers)
    elif symbol == '-':
        return reduce(lambda a, b: a - b, numbers)
    elif symbol == '*':
        return reduce(lambda a, b: a * b, numbers)
    elif symbol == '/':
        return reduce(lambda a, b: a / b, numbers)




print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))