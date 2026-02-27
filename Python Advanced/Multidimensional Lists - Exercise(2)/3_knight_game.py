size = int(input())
matrix = [list(input()) for _ in range(size)]

possible_moves = ((-2,-1), (-2, 1), (2, 1), (2, -1), (-1,-2), (1, -2), (1, 2), (-1, 2))
removed_knights = 0
knight_with_most_attacks = []
strongest_knight = 0
knight_counter = 0


while True:
        max_attacks = 0
        knight_with_most_attacks = []
        for row in range(size):
            for col in range(size):
                if matrix[row][col] == "K":
                    knight_counter = 0

                    for move in possible_moves:

                        current_row = row + move[0]
                        current_col = col + move[1]
                        if 0 <= current_row < size and 0 <= current_col < size:

                            if matrix[current_row][current_col] == "K":
                                knight_counter += 1
                    if knight_counter > max_attacks:
                        max_attacks = knight_counter
                        knight_with_most_attacks = [row, col]
        if knight_with_most_attacks:
            r,c = knight_with_most_attacks[0], knight_with_most_attacks[1]
            matrix[r][c] = "0"
            removed_knights += 1
        else:
            break

print(removed_knights)






