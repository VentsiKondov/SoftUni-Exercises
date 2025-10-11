names_of_gifts = input().split(" ")
command = ''
while command != "No money":
    command = input().split(" ")
    if command[0] == "OutOfStock":
        for index in range(len(names_of_gifts)):
            if command[1] == names_of_gifts[index]:
                names_of_gifts.pop(index)
                names_of_gifts.insert(index, "None")
    elif command[0] == "JustInCase":
        names_of_gifts[-1] = command[1]
    elif command[0] == "Required":
        if int(command[2]) <= len(names_of_gifts)-1:
            names_of_gifts[int(command[2])] = command[1]
    else:
        break

for name in names_of_gifts:
    if name == "None":
        names_of_gifts.remove(name)

print(" ".join(names_of_gifts))

# for names in names_of_gifts:
#     for index in range(len(names)):
#         if names == command[1]:
#             names_of_gifts.remove(command[1])
#             command = "None"
#             names_of_gifts.insert(index, command)
#         else:
#             continue
