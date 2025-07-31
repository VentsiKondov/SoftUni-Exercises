lily_age = int(input())
washing_machine_price = float(input())
price_per_toy = int(input())

saved_money = 0
toy_count = 0
even_day_counter = 1

for age in range(1, lily_age+ 1):
    if age % 2 == 0:
        saved_money += 10 * even_day_counter
        saved_money -=1
        even_day_counter += 1
    elif age % 2 == 1:
        toy_count += 1


total_sum = saved_money + (toy_count * price_per_toy)
if total_sum >= washing_machine_price:
    print(f"Yes! {total_sum-washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price-total_sum:.2f}")