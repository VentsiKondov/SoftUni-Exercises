number_of_orders = int(input())
total_price = 0
all_correct = False

for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules = int(input())
    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules <= 2000:
        all_correct = True
    if all_correct:
        coffee_price = 0
        coffee_price += days * price_per_capsule * capsules
        total_price += coffee_price
        print(f'The price for the coffee is: ${coffee_price:.2f}')


print(f"Total: ${total_price:.2f}")


