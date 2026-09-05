

my_dictionary = {}

while True:
    command = input()
    if command == 'stop':
        break
    quantity = int(input())
    ore = command
    my_dictionary[ore] = my_dictionary.get(ore, 0) + quantity
    # if ore not in my_dictionary:
    #     my_dictionary[ore] = 0
    # my_dictionary[ore] += quantity

for key, value in my_dictionary.items():
    print(f'{key} -> {value}')














