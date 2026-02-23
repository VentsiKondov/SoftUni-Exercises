from collections import deque




rows ,columns = [int(x) for x in input().split(' ')]
snake = deque(input())
my_matrix = []
for row in range(rows):
    my_matrix.append(['']*columns)
    for col in range(columns):
        if row % 2 ==0:
            my_matrix[row][col] = snake[0]
        else:
            my_matrix[row][-1-col] = snake[0]
        snake.rotate(-1)

for row in my_matrix:
    print(*row, sep='')