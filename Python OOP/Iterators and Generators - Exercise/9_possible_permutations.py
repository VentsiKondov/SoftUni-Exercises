from itertools import permutations


def possible_permutations(list_of_numbers):
    for row in permutations(list_of_numbers):
        yield list(row)


[print(n) for n in possible_permutations([1, 2, 3])]