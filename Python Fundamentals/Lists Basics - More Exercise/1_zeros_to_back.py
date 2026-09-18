numbers = list(map(int, input().split(', ')))
filtered_numbers = list(filter(lambda x: x != 0, numbers))

for _ in range(numbers.count(0)):
    filtered_numbers.append(0)

print(filtered_numbers)