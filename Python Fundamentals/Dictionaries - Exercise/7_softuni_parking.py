def register(name, license_number):
    if name not in my_dictionary:
        my_dictionary[name] = license_number
        return f'{name} registered {license_number} successfully'
    else:
        return f'ERROR: already registered with plate number {license_number}'


def unregister(name):
    if name not in my_dictionary:
        return f"ERROR: user {name} not found"
    else:
        del my_dictionary[name]
        return f"{name} unregistered successfully"


my_dictionary = {}
number_of_commands = int(input())
for _ in range(number_of_commands):
    commands = input().split()
    command = commands[0]
    name = commands[1]
    if command == 'register':
        license_number = commands[2]
        print(register(name, license_number))
    elif command == 'unregister':
        print(unregister(name))

for key, value in my_dictionary.items():
    print(f"{key} => {value}")
