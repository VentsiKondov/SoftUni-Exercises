n1 = int(input())
n2 = int(input())
operator = input()

def even_or_odd(result):
    if result % 2 == 0:
        return "even"
    else:
        return "odd"


if operator == "+":
    result = n1 + n2
    print(f'{n1} + {n2} = {n1 + n2} - {even_or_odd(result)}')
elif operator == "-":
    result = n1 - n2
    print(f'{n1} - {n2} = {n1 - n2} - {even_or_odd(result)}')
elif operator == "*":
    result = n1 * n2
    print(f'{n1} * {n2} = {n1 * n2} - {even_or_odd(result)}')
elif operator == "/":
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        result = n1 / n2
        print(f'{n1} / {n2} = {n1 / n2:.2f}')
elif operator == "%":
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        result = n1 % n2
        print(f'{n1} % {n2} = {n1 % n2}')




