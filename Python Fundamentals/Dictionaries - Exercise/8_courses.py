command = input().split(" : ")
my_dictionary = {}
while len(command) > 1:
    course_name = command[0]
    student_name = command[1]
    if course_name not in my_dictionary:
        my_dictionary[course_name] = []
        my_dictionary[course_name].append(student_name)
    else:
        my_dictionary[course_name].append(student_name)
    command = input().split(" : ")

for key, value in my_dictionary.items():
    print(f"{key}: {len(my_dictionary[key])}")
    for item in value:
        print(f'-- {item}')
