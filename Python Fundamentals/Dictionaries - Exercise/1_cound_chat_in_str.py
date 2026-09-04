words = input().split()
my_dictionary = {}

for word in words:
    for letter in word:
        if letter not in my_dictionary:
            my_dictionary[letter] = 1
        elif letter in my_dictionary:
            my_dictionary[letter] += 1

for key, value in my_dictionary.items():
    print(f'{key} -> {value}')