rows ,cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_cols = range(cols)

def is_valid(info):
    if {info[0], info[2]}.issubset(valid_rows) and {info[1], info[3]}.issubset(valid_cols):
        return True
    return False


def swap(info,command):
    if is_valid(info) and  command == "swap" and len(info) == 4:
        row1,col1,row2,col2 = info
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for row in matrix:
            print(*row, end="\n")
    else:
        print("Invalid input!")



while True:
    command, *info = [int(x) if x.isdigit() else x for x in input().split()]

    if command == "END":
        break

    if command == "swap":
        swap(info, command)

    else:
        print("Invalid input!")