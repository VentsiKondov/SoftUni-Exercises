points = int(input())
bonus_points = 0
total_points = 0
if points <= 100:
    bonus_points = 5
elif 100< points <= 1000:
    bonus_points = 0.2 * points
else:
    bonus_points = 0.1 * points

if points % 2 ==0:
    bonus_points += 1
elif points % 10 ==5:
    bonus_points += 2
total_points = bonus_points + points
print(bonus_points)
print(total_points)
