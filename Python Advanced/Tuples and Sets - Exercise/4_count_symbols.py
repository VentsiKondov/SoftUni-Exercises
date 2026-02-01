text = input()
my_dict = {}
for letter in text:
    if letter not in my_dict:
        my_dict[letter] = 0
    my_dict[letter] += 1

for letter, count in sorted(my_dict.items()):
    print(f"{letter}: {count} time/s")