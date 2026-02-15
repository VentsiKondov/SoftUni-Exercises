rows = int(input())
my_matrix = []
res =[]

for i in range(rows):
    my_matrix.append(list(input()))

target = input()

for r in range(rows):
    for c in range(rows):
        if my_matrix[r][c] == target:
            res.append((r,c))
            print(*res)
            exit()
else:
    print(f"{target} does not occur in the matrix")

