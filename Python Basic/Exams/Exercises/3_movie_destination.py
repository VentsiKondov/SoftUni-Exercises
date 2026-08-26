budget = float(input())
destination = input()
season = input()
days = int(input())
price = 0

if season == "Winter":
    if destination == "Dubai":
        price = 45000
    elif destination == "Sofia":
        price = 17000
    elif destination == "London":
        price = 24000
elif season == "Summer":
    if destination == "Dubai":
        price = 40000
    elif destination == "Sofia":
        price = 12500
    elif destination == "London":
        price = 20250

price*= days
if destination == "Dubai":
    price = price - (price * 0.3)
elif destination == "Sofia":
    price = price + (price * 0.25)

diff = abs(budget - price)
if budget >= price:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")