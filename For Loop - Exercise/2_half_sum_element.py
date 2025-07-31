import sys

numbers = int(input())
max_num = -sys.maxsize
sum_num = 0
for num in range(numbers):
    number = int(input())
    if number > max_num:
        max_num = number
    sum_num += number

if max_num == sum_num - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    sum_num = sum_num - max_num
    print("No")
    print(f"Diff = {abs(max_num - sum_num)}")