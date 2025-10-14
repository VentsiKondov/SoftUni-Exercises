ticket_cost = 150
items_with_prices = input().split("|")
budget = float(input())
new_item_price = 0
profit = 0
total_profit = 0
total_price = 0
for i in items_with_prices:
    items = i.split("->")
    item = items[0]
    price = float(items[1])
    if budget >= price:
        if item == "Clothes" and price <= 50:
            new_item_price = price * 0.4 + price
            profit = new_item_price - price
            budget -= price
            print(f"- {new_item_price:.2f}")
            total_profit += profit
            total_price += new_item_price
        elif item == "Shoes" and price <= 35:
            new_item_price = price * 0.4 + price
            profit = new_item_price - price
            budget -= price
            print(f"- {new_item_price:.2f}")
            total_profit += profit
            total_price += new_item_price
        elif item == "Accessories" and price <= 20.50:
            new_item_price = price * 0.4 + price
            profit = new_item_price - price
            budget -= price
            print(f"- {new_item_price:.2f}")
            total_profit += profit
            total_price += new_item_price

print(f"Profit:{total_profit:.2f}")
if total_price + budget >= ticket_cost:
    print("Hello, France!")
else:
    print("Not enough money!")