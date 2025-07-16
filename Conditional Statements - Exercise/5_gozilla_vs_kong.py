film_budget = float(input())
extra_count = int(input())
price_per_one_extra = float(input())
extra_price = extra_count * price_per_one_extra
decor_price = 0.1 * film_budget
if extra_count > 150:
    extra_price = extra_price - extra_price*0.1
if decor_price + extra_price > film_budget:
    print("Not enough money!")
    print(f"Wingard needs {((decor_price + extra_price) - film_budget):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {(film_budget - (decor_price + extra_price)):.2f} leva left.")