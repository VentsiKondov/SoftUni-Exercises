days = int(input()) - 1
room = input()
grade = input()
price = 0
final_price = 0

if room == "room for one person":
    price = days * 18
elif room == "apartment":
    price = days * 25
    if days < 10:
        price -= price * 0.3
    elif 10<=days <= 15:
        price -= price * 0.35
    elif days > 15:
        price -= price * 0.5
elif room == "president apartment":
    price = days * 35
    if days < 10:
        price -= price * 0.1
    elif 10<=days <= 15:
        price -= price * 0.15
    elif days > 15:
        price -= price * 0.2

if grade == "positive":
    final_price = price + price * 0.25
elif grade == "negative":
    final_price = price - price * 0.1

print(f'{final_price:.2f}')