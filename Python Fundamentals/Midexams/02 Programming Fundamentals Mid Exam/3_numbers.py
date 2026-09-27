numbers = list(map(int, input().split()))

average_number = sum(numbers) / len(numbers)
result = [num for num in numbers if num > average_number]
sorted_numbers = sorted(result, reverse=True)
if result:
    if len(result) <=5:
        print(*sorted_numbers)
    else:

        print(*sorted_numbers[:5])

else:
    print('No')
