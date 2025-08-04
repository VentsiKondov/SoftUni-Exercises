command = input()
balance = 0

while command != "NoMoreMoney":
    money = float(command)
    if money < 0:
        print('Invalid operation!')
        break
    else:
        print(f"Increase: {money:.2f}")
    balance += money
    command = input()

print(f"Total: {balance:.2f}")