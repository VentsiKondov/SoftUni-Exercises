size = int(input())
matrix = []
bunny_pos = []
for row in range(size):
    matrix.append(input().split())

    if "B" in matrix[row]:
        bunny_pos = [row, matrix[row].index("B")]

directions = {"up": [-1,0], "down": [1,0], "left": [0,-1], "right": [0,1]}
best_direction = None
maximum_eggs = 0
best_positions = []

for direction, idx in directions.items():
    current_pos = [ bunny_pos[0]+ idx[0], idx[1] + bunny_pos[1] ]
    current_eggs = 0
    positions = []
    while 0<=current_pos[0] < size and 0 <=current_pos[1] < size:


        if matrix[current_pos[0]][current_pos[1]].isdigit():
            current_eggs += int(matrix[current_pos[0]][current_pos[1]])
            positions.append([current_pos[0], current_pos[1]])


        elif matrix[current_pos[0]][current_pos[1]] == "X":
            break

        current_pos[0] += idx[0]
        current_pos[1] += idx[1]



    if current_eggs >= maximum_eggs:
        maximum_eggs = current_eggs
        best_direction = direction
        best_positions = positions


print(best_direction)
print(*best_positions, sep="\n")
print(maximum_eggs)

