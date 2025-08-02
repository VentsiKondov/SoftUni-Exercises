
from math import \
    floor

number_of_tournaments = int(input())
beginning_points = int(input())
number_of_wins = 0
average_points = 0


final_points = beginning_points

tournament = {
    "W": 2000,
    "F": 1200,
    "SF": 720
}

for _ in range(number_of_tournaments):
    current_status = input()
    if current_status in tournament:
        final_points += tournament[current_status]

    average_points += tournament[current_status]

    if current_status == "W":
        number_of_wins += 1

print(f"Final points: {final_points}")
print(f"Average points: {floor(average_points / number_of_tournaments)}")
print(f"{(number_of_wins / number_of_tournaments) * 100:.2f}%")