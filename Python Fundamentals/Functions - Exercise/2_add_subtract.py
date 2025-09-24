def sum_numbers(num1, num2):
    return num1 + num2
def subtract_numbers(sum_numbers, num3):
    return sum_numbers(num1, num2) - num3


num1 = int(input())
num2 = int(input())
num3 = int(input())
sum_numbers(num1, num2)
print(sum_numbers(num1, num2))
print(subtract_numbers(sum_numbers, num3))