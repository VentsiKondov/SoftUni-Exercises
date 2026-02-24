from collections import \
    deque


def moving(row,col,value,my_matrix):

    for r,c in positions.values():
        temp_row = r+row
        temp_col = c+col
        if temp_row < 0 or temp_row >= rows:
            continue
        if temp_col < 0 or temp_col >= rows:
            continue
        if my_matrix[temp_row][temp_col] > 0:
            my_matrix[temp_row][temp_col] = -value + my_matrix[temp_row][temp_col]




def explosion(row,col,my_matrix):
    bomb_value = my_matrix[row][col]
    if bomb_value > 0:
        my_matrix[row][col] = 0
        moving(row,col,bomb_value,my_matrix)

rows = int(input())
my_matrix = []


for _ in range(rows):
    text = input().split()
    my_matrix.append([int(x) for x in text])


all_bombs = deque(input().split())
positions = {
    'up':(-1,0),
    'upright':(-1,1),
    'upleft':(-1,-1),
    'down':(1,0),
    'downright':(1,1),
    'downleft':(1,-1),
    'left':(0,-1),
    'right':(0,1),
}


for i in range(len(all_bombs)):
    current_bomb = all_bombs[i]
    bomb_row = int(current_bomb.split(',')[0])
    bomb_col = int(current_bomb.split(',')[1])
    explosion(bomb_row,bomb_col,my_matrix)


alive_counter = 0
total_sum = 0
for row in my_matrix:
    for number in row:
        if number > 0:
            alive_counter += 1
            total_sum += number

print(f"Alive cells: {alive_counter}")
print(f"Sum: {total_sum}")
[print(*row) for row in my_matrix]