vacation_price = float(input())
number_of_puzzles=  int(input())
number_of_dolls = int(input())
number_of_teddy_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

total_price = number_of_puzzles*2.6 + number_of_trucks*2 + number_of_minions*8.2 + number_of_dolls*3 + number_of_teddy_bears*4.1
all_of_them = number_of_trucks + number_of_minions + number_of_dolls + number_of_teddy_bears + number_of_puzzles
if all_of_them >= 50:
    total_price = total_price - total_price*0.25

total_price = total_price - total_price*0.1
if total_price >= vacation_price:
    print(f"Yes! {total_price-vacation_price:.2f} lv left.")
else:
    print(f"Not enough money! {vacation_price-total_price:.2f} lv needed.")