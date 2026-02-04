odd_set = set()
even_set = set()


for row in range(1, int(input())+ 1):
    name_value = sum(ord(letter) for letter in input()) // row
    if name_value % 2 == 0:
        even_set.add(name_value)
    else:
        odd_set.add(name_value)

if sum(odd_set) == sum(even_set):
    print(*even_set.union(odd_set), sep=", ")
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")
elif sum(even_set) > sum(odd_set):
    print(*even_set.symmetric_difference(odd_set), sep=", ")