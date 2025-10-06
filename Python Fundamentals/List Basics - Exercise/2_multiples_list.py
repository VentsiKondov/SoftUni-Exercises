factor = int(input())
length_of_list = int(input())
list_with_numbers = []

for num in range(1,length_of_list+1):
    list_with_numbers.append(factor*num)

print(list_with_numbers)