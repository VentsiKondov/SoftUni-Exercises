lst_with_numbers = list(map(int, input().split()))
command = input().split()

def swap_command(index1, index2):
    lst_with_numbers[index1], lst_with_numbers[index2] = lst_with_numbers[index2], lst_with_numbers[index1]
    return lst_with_numbers

def multiply_command(index1, index2):
    number = lst_with_numbers[index1] * lst_with_numbers[index2]
    lst_with_numbers.pop(index1)
    lst_with_numbers.insert(index1, number)
    return lst_with_numbers

while command[0] != 'end':
    full_command = command[0]
    if full_command == 'swap':
        first_index = int(command[1])
        second_index = int(command[2])
        lst_with_numbers = swap_command(first_index, second_index)
    elif full_command == 'multiply':
        first_index = int(command[1])
        second_index = int(command[2])
        lst_with_numbers = multiply_command(first_index, second_index)
    elif full_command == 'decrease':
        lst_with_numbers = [num-1 for num in lst_with_numbers]
    command = input().split()

result = ', '.join(map(str, lst_with_numbers))
print(result)