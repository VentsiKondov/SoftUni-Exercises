type_flowers = input()
number_of_flowers = int(input())
budget = int(input())
total_sum = 0
if type_flowers == "Roses":
    total_sum = number_of_flowers * 5
    if number_of_flowers > 80:
        total_sum = total_sum - total_sum * 0.1

elif type_flowers == "Dahlias":
    total_sum = number_of_flowers * 3.8
    if number_of_flowers > 90:
        total_sum = total_sum - total_sum * 0.15

elif type_flowers == "Tulips":
    total_sum = number_of_flowers * 2.8
    if number_of_flowers > 80:
        total_sum = total_sum - total_sum * 0.15

elif type_flowers == "Narcissus":
    total_sum = number_of_flowers * 3
    if number_of_flowers < 120:
        total_sum = total_sum + total_sum * 0.15

elif type_flowers == "Gladiolus":
    total_sum = number_of_flowers * 2.5
    if number_of_flowers < 80:
        total_sum = total_sum + total_sum * 0.2

difference = abs(budget - total_sum)

if budget >= total_sum:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")