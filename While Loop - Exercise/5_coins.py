change = float(input())
coins = 0
change = change * 100
for x in (200, 100, 50, 20, 10, 5, 2):
    current_coins = int(change / x)
    change -= current_coins * x
    coins += current_coins

current_coins = int(change)
coins += current_coins

print(coins)
