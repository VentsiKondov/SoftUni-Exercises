first_n = int(input())
second_n = int(input())

for number in range(first_n, second_n + 1):
    current_n = str(number)
    odd_sum = 0
    even_sum = 0
    for index, digit in enumerate(current_n):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if even_sum == odd_sum:
        print(number, end=" ")



