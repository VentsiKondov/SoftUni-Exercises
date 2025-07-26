
budget = int(input())
season = input()
number_of_fishers = int(input())
price = 0
total_price = 0
if season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600
elif season == "Spring":
    price = 3000



if 0 <=number_of_fishers <=6:
    total_price = price - price * 0.1
elif 7<=number_of_fishers <=11:
    total_price = price - price * 0.15
elif number_of_fishers >=12:
    total_price = price - price * 0.25

if number_of_fishers % 2 ==0 and season != "Autumn":
    final_sum = total_price - total_price * 0.05
else:
    final_sum = total_price
diff = abs(final_sum - budget)

if budget >= final_sum:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")