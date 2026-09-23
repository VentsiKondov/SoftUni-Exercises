

sequence_of_numbers = input().split()
command = input().split()
moves = 0

while command[0] != 'end':
    moves += 1
    first_index,second_index = int(command[0]), int(command[1])
    max_valid_index = len(sequence_of_numbers) - 1
    if first_index == second_index or (not 0<=first_index <=max_valid_index or not 0<=second_index <= max_valid_index):
        middle = int(len(sequence_of_numbers) / 2)
        sequence_of_numbers.insert(middle, f'-{moves}a')
        sequence_of_numbers.insert(middle, f'-{moves}a')
        print(f"Invalid input! Adding additional elements to the board")
        command = input().split()
        continue

    first_number = sequence_of_numbers[first_index]
    second_number = sequence_of_numbers[second_index]
    if first_number == second_number:
        print(f"Congrats! You have found matching elements - {sequence_of_numbers[first_index]}!")
        del sequence_of_numbers[first_index]
        if first_index < second_index:
            second_index -= 1
        del sequence_of_numbers[second_index]
    else:
        print('Try again!')

    if not sequence_of_numbers:
        print(f"You have won in {moves} turns!")
        exit()
    command = input().split()

print('Sorry you lose :(')
print(*sequence_of_numbers, sep=' ')