my_inverted_lst = []
numbers = input().split(' ')
for number in numbers:
    new_number = int(number)
    my_inverted_lst.append(-new_number)
print(my_inverted_lst)
