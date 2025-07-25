film = input()
rows = int(input())
columns = int(input())
price = 0
total_seats = rows * columns
total_sum = 0

if film == "Premiere":
    price = 12
elif film == "Normal":
    price = 7.5
elif film == "Discount":
    price = 5

total_sum = price * total_seats
print(f'{total_sum:.2f} leva')