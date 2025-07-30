lst_of_numbers = []

for num in range(int(input())):
    lst_of_numbers.append(int(input()))

print(f"Max number: {max(lst_of_numbers)}")
print(f"Min number: {min(lst_of_numbers)}")