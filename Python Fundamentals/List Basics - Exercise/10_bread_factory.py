initial_energy =100
coins = 100
events  = input().split("|")
print(events)
is_closed = False
gained_energy = 0

for event in events:
    new_pair = event.split("-")
    command = new_pair[0]
    num = int(new_pair[1])
    if command == "rest":
        if initial_energy + num > 100:
            initial_energy = 100
            gained_energy = 0
        else:
            initial_energy += num
            gained_energy = initial_energy - num
        print(f'You gained {num} energy.')
        print(f'Current energy: {initial_energy}')
    elif command == "order":
        initial_energy -= 30
        if initial_energy < 0:
            initial_energy = 0
        if initial_energy >= num:
            coins += num
            print(f'You earned {num} coins.')
        else:
            initial_energy += 50
            print("You had to rest")
    else:
        if coins >num:
            coins -= num
            print(f'You bought {command}')
        else:
            is_closed = True
            break
if is_closed:
    print(f'Closed! Cannot afford {command}')
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"energy: {initial_energy}")

