lst_with_numbers = list(map(int, input().split(', ')))
positive_numbers = [str(num) for num in lst_with_numbers if num >= 0]
negative_numbers = [str(num) for num in lst_with_numbers if num < 0]
even_numbers = [str(num) for num in lst_with_numbers if num %2 == 0]
odd_numbers = [str(num) for num in lst_with_numbers if num % 2== 1]
print(f'Positive numbers: {", ".join(positive_numbers)}')
print(f'Negative numbers: {", ".join(negative_numbers)}')
print(f'Even numbers: {", ".join(even_numbers)}')
print(f'Odd numbers: {", ".join(odd_numbers)}')