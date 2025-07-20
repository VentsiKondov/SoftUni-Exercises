plastic = int(input())
paint = int(input())
quantity_litres = int(input())
hours_to_complete = int(input())

plastic_sum = (plastic + 2) * 1.5
paint_sum = (paint + 0.1 * paint) * 14.5
litres_sum = quantity_litres * 5

total_sum = plastic_sum + paint_sum + litres_sum + 0.4


price_for_one_hour = 0.3 * total_sum
price_to_complete = price_for_one_hour * hours_to_complete
print(total_sum+ price_to_complete)