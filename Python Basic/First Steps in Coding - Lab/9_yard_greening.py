square_meters = float(input())
total_price = square_meters * 7.61
discount = total_price * 0.18
total_sum = total_price - discount
print(f"The final price is: {total_sum} lv.")
print(f"The discount is: {discount} lv.")