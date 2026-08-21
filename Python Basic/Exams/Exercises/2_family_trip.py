budget = float(input())
nights = int(input())
price_for_night = float(input())
bonus_taxes = int(input()) / 100

if nights > 7:
    price_for_night -= price_for_night * 0.05

total_price_for_nights = price_for_night * nights
taxes = budget * bonus_taxes
budget -= total_price_for_nights + taxes
if budget >= 0:
    print(f"Ivanovi will be left with {budget:.2f} leva after vacation.")
else:
    print(f"{abs(budget):.2f} leva needed.")