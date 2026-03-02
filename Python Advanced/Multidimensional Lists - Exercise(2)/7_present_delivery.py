number_of_presents = int(input())
rows = int(input())
my_matrix = []

total_good_kids = 0
good_kids_left = 0
santa_location = []


for i in range(rows):
    row = input().split()
    my_matrix.append(row)
    if "S" in row:
        santa_location = [i,row.index("S")]
    good_kids_left += row.count("V")

total_good_kids = good_kids_left

positions = {
    'up':(-1,0),
    'down':(1,0),
    'left':(0,-1),
    'right':(0,1),
}

my_matrix[santa_location[0]][santa_location[1]] = "-"


while number_of_presents > 0:
    command = input()
    if command == "Christmas morning":
        break

    r,c = positions[command]
    new_pos = [santa_location[0] + r,santa_location[1] + c]
    santa_location = [new_pos[0], new_pos[1]]

    if my_matrix[santa_location[0]][santa_location[1]] == "V":
        my_matrix[santa_location[0]][santa_location[1]] = "-"
        number_of_presents -= 1
        good_kids_left -= 1
    elif my_matrix[santa_location[0]][santa_location[1]] == "X":
        my_matrix[santa_location[0]][santa_location[1]] = "-"

    elif my_matrix[santa_location[0]][santa_location[1]] == "C":
        my_matrix[santa_location[0]][santa_location[1]] = "-"
        for pos in positions:
            r,c = positions[pos]
            temp_row = r + santa_location[0]
            temp_col = c + santa_location[1]
            if my_matrix[temp_row][temp_col] == "V":
                my_matrix[temp_row][temp_col] = "-"
                number_of_presents -= 1
                good_kids_left -= 1
            elif my_matrix[temp_row][temp_col] == "X":
                my_matrix[temp_row][temp_col] = "-"
                number_of_presents -= 1

            if number_of_presents <= 0:
                break
    if number_of_presents<=0:
        break

my_matrix[santa_location[0]][santa_location[1]] = 'S'
if number_of_presents <= 0 and good_kids_left > 0:
    print(f'Santa ran out of presents!')

[print(*row, sep=' ') for row in my_matrix]

if good_kids_left == 0:
    print(f'Good job, Santa! {total_good_kids} happy nice kid/s.')
else:
    print(f"No presents for {good_kids_left} nice kid/s.")




