lst_with_numbers = []
command = input()
while command != "Stop":
    lst_with_numbers.append(int(command))
    command = input()

print(min(lst_with_numbers))