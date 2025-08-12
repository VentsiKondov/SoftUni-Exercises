saved_money =0

while True:
    destination = input()

    if destination == 'End':
        break
    minimum_budget = float(input())
    saved_money = 0
    while saved_money < minimum_budget:
        saved_money += float(input())

    print(f"Going to {destination}!")










