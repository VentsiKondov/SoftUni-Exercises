wins = 0
losses = 0
total_matches = 0

while True:
    command = input()
    if command == 'End of tournaments':
        break

    tournament_name = command
    matches = int(input())
    total_matches += matches
    for match in range(1, matches+1):
        first_team_score = int(input())
        second_team_score = int(input())
        if first_team_score > second_team_score:
            wins += 1
            print(f"Game {match} of tournament {tournament_name}: win with {first_team_score - second_team_score} points.")
        elif second_team_score > first_team_score:
            losses += 1
            print(f"Game {match} of tournament {tournament_name}: lost with {second_team_score - first_team_score} points.")

print(f"{wins/total_matches * 100:.2f}% matches win")
print(f"{losses/total_matches * 100:.2f}% matches lost")
