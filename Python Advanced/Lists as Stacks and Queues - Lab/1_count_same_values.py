numbers = [float(x) for x in input().split()]
my_dict = {}

for number in numbers:
    my_dict[number] = my_dict.get(number, 0) + 1

[print(f"{k:.1f} - {v} times") for k, v in my_dict.items()]
