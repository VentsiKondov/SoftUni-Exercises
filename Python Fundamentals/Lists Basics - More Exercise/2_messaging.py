numbers = input().split()
text = input()
new_numbers = []
my_list = []
for number in numbers:
    current_index = sum([int(num) for num in number])
    if current_index >= len(text):
        current_index -= len(text)
    my_list.append(text[current_index])
    text = text[:current_index] + text[current_index + 1:]


print(''.join(my_list))