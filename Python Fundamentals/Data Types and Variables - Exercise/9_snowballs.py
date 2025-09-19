my_lst = []
lst_with_numbers = []

index_with_max_value = 0
max_value = 0

for _ in range(int(input())):
    snowball_weight = int(input())
    time_needed = int(input())
    quality_of_snowball = int(input())

    value = (snowball_weight // time_needed) ** quality_of_snowball
    my_lst.append(f"{snowball_weight} : {time_needed} = {value} ({quality_of_snowball})")
    lst_with_numbers.append(value)

for index, value in enumerate(lst_with_numbers):
    if value > max_value:
        max_value = value
        index_with_max_value = index

print(my_lst[index_with_max_value])