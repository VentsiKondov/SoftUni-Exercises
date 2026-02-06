from collections import \
    deque

chocolates = deque([int(x) for x in input().split(", ")])
cups_of_milk =deque([int(x) for x in input().split(", ")])
milkshake = 0

while chocolates and cups_of_milk:
    if milkshake == 5:
        break
    last_chocolate = chocolates.pop()
    first_cup_of_milk = cups_of_milk.popleft()
    if last_chocolate <= 0 and first_cup_of_milk <= 0:
        continue
    if last_chocolate <= 0:
        cups_of_milk.appendleft(first_cup_of_milk)
        continue
    if first_cup_of_milk <= 0:
        chocolates.append(last_chocolate)
        continue

    if last_chocolate == first_cup_of_milk:
        milkshake += 1
    else:
        cups_of_milk.append(first_cup_of_milk)
        chocolates.append(last_chocolate-5)

if milkshake == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(map(str, cups_of_milk))}")
else:
    print("Milk: empty")