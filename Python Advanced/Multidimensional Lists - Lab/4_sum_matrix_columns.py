rows,cols = [int(x) for x in input().split(', ')]
my_matrix = []

for i in range(rows):
    my_matrix.append([int(x) for x in input().split(' ')])

res = 0
for col in range(cols):
    for row in range(rows):
        res += my_matrix[row][col]
    print(res)
    res = 0


