

command = input().split("-")
my_dictionary = {}
second_dictionary = {}
language_lst = []
count = 1

while len(command) > 1:

    username = command[0]
    if "banned" in command:
       username = command[0]
       del my_dictionary[username]
       command = input().split("-")
       continue
    language = command[1]
    points  = int(command[2])

    if language not in second_dictionary.keys():
        second_dictionary[language] = count
    else:
        second_dictionary[language] += count


    if username not in my_dictionary:
        my_dictionary[username] = points

    else:

        if my_dictionary[username] <= points:
            my_dictionary[username] = points
    command = input().split("-")

print(my_dictionary.items())

# print("Results:")
for name, points in my_dictionary.items():
        print(f"{name} | {points}")
print("Submissions")
for k, v in second_dictionary.items():
    print(f"{k} - {v}")




