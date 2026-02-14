rows = int(input())
my_matrix = []
for i in range(rows):
    my_matrix.append([int(x) for x in input().split(' ')])

res = 0

cur_row = 0
cur_col = 0
while cur_row < rows and cur_col < rows:
    res += my_matrix[cur_row][cur_col]
    cur_row += 1
    cur_col += 1
print(res)