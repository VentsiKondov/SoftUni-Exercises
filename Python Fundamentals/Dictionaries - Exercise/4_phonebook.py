phone_number = input()
my_dictionary = {}
while not phone_number.isdigit():
    name, phone = phone_number.split('-')
    my_dictionary[name] = phone
    phone_number = input()


for i in range(int(phone_number)):
    first_name = input()
    if first_name in my_dictionary:
        print(f'{first_name} -> {my_dictionary[first_name]}')
    else:
        print(f'Contact {first_name} does not exist.')

