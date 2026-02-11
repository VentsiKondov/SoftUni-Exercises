rows = int(input())

my_matrix = []
res = []
for i in range(rows):
    my_matrix.append([int(x) for x in input().split(', ') if int(x) % 2 == 0])
    res.extend(my_matrix)
    my_matrix = []

print(res)