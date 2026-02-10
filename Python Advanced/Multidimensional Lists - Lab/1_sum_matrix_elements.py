rows,cols = [int(x) for x in input().split(', ')]
my_matrix = []
total = 0
for _ in range(rows):
    items = [int(i) for i in input().split(', ')]
    my_matrix.append(items)
    total += sum(i for i in items)

print(total)
print(my_matrix)