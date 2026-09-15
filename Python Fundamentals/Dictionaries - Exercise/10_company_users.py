command = input().split(" -> ")
my_dictionary = {}
while len(command) > 1:
    company_name = command[0]
    employee_id = command[1]
    if company_name not in my_dictionary:
        my_dictionary[company_name] = []
        my_dictionary[company_name].append(employee_id)
    else:
        if employee_id not in my_dictionary[company_name]:
            my_dictionary[company_name].append(employee_id)
    command = input().split(" -> ")

for key, value in my_dictionary.items():
    print(f"{key}")
    for item in value:
        print(f'-- {item}')