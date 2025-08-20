money_needed_for_the_vacation = float(input())
current_money = float(input())
days = 0
spend_days =0

while spend_days < 5:
    command = input()
    money = float(input())
    days += 1
    if command == "save":
        spend_days = 0
        current_money += money
        if current_money >= money_needed_for_the_vacation:
            print(f"You saved the money for {days} days.")
            break

    if command == "spend":
        current_money -= money
        spend_days += 1
        if current_money <= 0:
            current_money = 0
else:
    print("You can't save the money.")
    print(days)



