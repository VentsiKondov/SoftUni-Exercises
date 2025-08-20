sum_of_first_two = 0
sum_of_second_two = 0
range_numbers = int(input())
for number in range(range_numbers*2):
    number_to_add = int(input())
    if number < range_numbers:
        sum_of_first_two += number_to_add
    elif number >= range_numbers:
        sum_of_second_two += number_to_add

if sum_of_first_two == sum_of_second_two:
    print(f"Yes, sum = {sum_of_first_two}")
else:
    print(f"No, diff = {abs(sum_of_first_two - sum_of_second_two)}")
