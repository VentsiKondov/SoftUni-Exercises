month = input()
overnight_stay = int(input())
discount = 0
studio_discount = 0
studio_price = 0
apartment_price = 0
apartment_discount = 0
if month == "October" or month == 'May' :
    studio_price = overnight_stay * 50
    apartment_price = overnight_stay * 65
elif month == "June" or month == 'September':
    studio_price = overnight_stay * 75.20
    apartment_price = overnight_stay * 68.70
elif month == "July" or month == 'August':
    studio_price = overnight_stay * 76
    apartment_price = overnight_stay * 77

if 7<overnight_stay <= 14 and (month == 'May' or month == "October"):
    studio_discount = 0.05
elif overnight_stay > 14 and (month == 'May' or month == "October"):
    studio_discount = 0.3
elif overnight_stay > 14 and (month == "June" or month == "September"):
    studio_discount = 0.2

if overnight_stay > 14:
    apartment_discount = 0.1

studio_total_price = studio_price - studio_price * studio_discount
apartment_total_price = apartment_price - apartment_price * apartment_discount

print(f"Apartment: {apartment_total_price:.2f} lv.")
print(f"Studio: {studio_total_price:.2f} lv.")

