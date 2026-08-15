number_of_joinery = int(input())
type_of_joinery = input()
type_of_delivery = input()

price_for_one = 0
discount = 0
total = 0

if number_of_joinery < 10:
    print("Invalid order")
    exit()

total = number_of_joinery

if type_of_joinery == '90X130':
    price_for_one = 110
    total *= price_for_one
    if number_of_joinery > 60:
        total  *= 0.92
    elif number_of_joinery > 30:
        total  *= 0.95
elif type_of_joinery == '100X150':
    price_for_one = 140
    total *= price_for_one
    if number_of_joinery > 80:
        total  *= 0.90
    elif number_of_joinery > 40:
        total  *= 0.94
elif type_of_joinery == '130X180':
    price_for_one = 190
    total *= price_for_one
    if number_of_joinery > 50:
        total  *= 0.88
    elif number_of_joinery > 20:
        total  *= 0.93
elif type_of_joinery == '200X300':
    price_for_one = 250
    total *= price_for_one
    if number_of_joinery > 50:
        total  *= 0.86
    elif number_of_joinery > 25:
        total  *= 0.91

if type_of_delivery == "With delivery":
    total += 60

if number_of_joinery > 99:
    total *= 0.96

print(f"{total:.2f} BGN")