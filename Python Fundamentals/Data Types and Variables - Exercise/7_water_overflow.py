WATER_TANK_CAPACITY = 255
current_liters = 0
for _ in range(int(input())):
    liters_of_water = int(input())

    if current_liters + liters_of_water > WATER_TANK_CAPACITY:
        print("Insufficient capacity!")
        continue

    current_liters += liters_of_water

print(current_liters)