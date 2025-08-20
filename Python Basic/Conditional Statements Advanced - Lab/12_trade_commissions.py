city = input()
commission = float(input())
final_commission = 0
cities = "Sofia Varna Plovdiv"
is_wrong = False
if city not in cities or commission < 0:
    is_wrong = True


if city == "Sofia":
    if 0<= commission <= 500:
        final_commission = commission * 0.05
    elif 500< commission <= 1000:
        final_commission = commission * 0.07
    elif 1000< commission <= 10000:
        final_commission = commission * 0.08
    else:
        final_commission = commission * 0.12

elif city == "Varna":
    if 0<= commission <= 500:
        final_commission = commission * 0.045
    elif 500< commission <= 1000:
        final_commission = commission * 0.075
    elif 1000< commission <= 10000:
        final_commission = commission * 0.1
    else:
        final_commission = commission * 0.13

elif city == "Plovdiv":
    if 0<= commission <= 500:
        final_commission = commission * 0.055
    elif 500< commission <= 1000:
        final_commission = commission * 0.08
    elif 1000< commission <= 10000:
        final_commission = commission * 0.12
    else:
        final_commission = commission * 0.145

if is_wrong:
    print("error")
else:
    print(f"{final_commission:.2f}")