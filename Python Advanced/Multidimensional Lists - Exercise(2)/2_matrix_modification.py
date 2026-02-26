rows =int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
command = input().split()
while command[0] != "END":
    type_command, row, col, value = command[0], int(command[1]), int(command[2]), int(command[3])
    if not (0 <= row < rows and 0 <= col < rows):
        print("Invalid coordinates")

    elif type_command == "Add":
        matrix[row][col] += value

    elif type_command == "Subtract":
        matrix[row][col] -= value

    command = input().split()


[print(*row) for row in matrix]