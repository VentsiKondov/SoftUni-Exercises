from math import \
    floor

number_of_tournaments = int(input())
beginning_points = int(input())
total_points = beginning_points
points_total_matches = 0
wins = 0

def tournament_points(tournament, total_points, points_total_matches, wins):
    if tournament == "W":
        total_points += 2000
        points_total_matches += 2000
        wins += 1
    elif tournament == "F":
        total_points += 1200
        points_total_matches += 1200
    elif tournament == "SF":
        total_points += 720
        points_total_matches += 720
    return total_points, points_total_matches, wins


for _ in range(number_of_tournaments):
    tournament = input()
    total_points, points_total_matches, wins = tournament_points(tournament, total_points, points_total_matches,wins)

print(f"Final points: {total_points}")
print(f"Average points: {floor(points_total_matches/ number_of_tournaments)}")
print(f"{(wins/number_of_tournaments)*100:.2f}%")
