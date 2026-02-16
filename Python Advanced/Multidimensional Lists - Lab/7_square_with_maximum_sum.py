def invalid_indices(current_row, current_col):
    if current_row + 1 < rows and current_col + 1 < cols:
        return False
    else:
        return True

max_sum = 0
first_row = []
second_row = []

rows, cols = [int(x) for x in input().split(', ')]
my_matrix = []
for i in range(rows):
    my_matrix.append([int(x) for x in input().split(', ')])

for r in range(rows):
    for c in range(cols):
        if not invalid_indices(r, c):
            current_number = my_matrix[r][c]
            right_number = my_matrix[r][c + 1]
            down_number = my_matrix[r+1][c]
            diagonal_num = my_matrix[r+1][c +1]
            total = current_number + right_number + down_number + diagonal_num
            if total > max_sum:
                max_sum = total
                first_row = [current_number, right_number]
                second_row = [down_number, diagonal_num]

print(*first_row)
print(*second_row)
print(max_sum)


