text = input()
new_lst = []
for character in text:
    if not new_lst:
        new_lst.append(character)
    elif character != new_lst[-1]:
        new_lst.append(character)

print(''.join(new_lst))