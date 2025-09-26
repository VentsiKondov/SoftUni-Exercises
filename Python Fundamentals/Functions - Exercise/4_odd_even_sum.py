def odd_even_sum(num):
    even_sum = 0
    odd_sum = 0
    for n in num:
        if int(n) % 2 == 0:
            even_sum += int(n)
        elif int(n) % 2 == 1:
            odd_sum += int(n)
    return even_sum, odd_sum




number = input()
even_sum, odd_sum = odd_even_sum(number)
print(f'Odd sum = {odd_sum}, even sum = {even_sum}')