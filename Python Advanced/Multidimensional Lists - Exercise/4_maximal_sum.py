rows , cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

def matrix_with_biggest_sum(matrix):
    biggest_sum = float('-inf')
    old_sum = 0
    new_lst = []
    for row in range(rows - 2):
        for col in range(cols - 2):
            first_row = matrix[row][col:col+3]
            second_row = matrix[row + 1][col:col+3]
            third_row = matrix[row + 2][col:col+3]
            old_sum = sum(first_row)+sum(second_row)+sum(third_row)
            if old_sum > biggest_sum:
                biggest_sum = old_sum
                new_lst = [first_row, second_row, third_row]
    return biggest_sum , new_lst
big_sum , new_lst = matrix_with_biggest_sum(matrix)
print(f"Sum = {big_sum}")
for row in new_lst:
    print(*row)