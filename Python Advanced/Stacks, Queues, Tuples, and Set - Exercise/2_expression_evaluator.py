from functools import reduce
import math
randon_expression = input().split()
idx= 0
calc = {"*": lambda i: reduce(lambda x,y: int(x) * int(y), randon_expression[:i]),
        "+": lambda i: reduce(lambda x,y: int(x) + int(y), randon_expression[:i]),
        "-": lambda i: reduce(lambda x,y: int(x) - int(y), randon_expression[:i]),
        "/": lambda i: reduce(lambda x,y: int(x) // int(y), randon_expression[:i])}





while idx < len(randon_expression):
    element = randon_expression[idx]
    if element in "*+-/":
        result = calc[element](idx)
        [randon_expression.pop(1) for _ in range(idx)]
        randon_expression[0] = str(result)
        idx = 0
    else:
        idx += 1


print("".join(randon_expression))