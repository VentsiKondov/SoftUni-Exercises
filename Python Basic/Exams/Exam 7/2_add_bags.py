price_for_baggage_over_20_kilos = float(input())
kilograms = float(input())
days_left = int(input())
number_of_bags = int(input())

total = 0



if kilograms < 10:
    total += price_for_baggage_over_20_kilos * 0.2
elif 10<=kilograms <= 20:
    total += price_for_baggage_over_20_kilos * 0.5
elif kilograms > 20:
    total += price_for_baggage_over_20_kilos

if days_left < 7:
    total += total * 0.4
elif 7<=days_left <= 30:
    total += total * 0.15
elif days_left > 30:
    total += total * 0.1


total = total * number_of_bags
print(f"The total price of bags is: {total:.2f} lv. ")