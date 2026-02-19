rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]
counter = 0

for row in range(rows - 1):
    for col in range(cols-1):
        current_symbol = matrix[row][col]
        if current_symbol == matrix[row][col+1] and current_symbol == matrix[row+1][col] and current_symbol == matrix[row+1][col+1]:
            counter += 1

print(counter)

