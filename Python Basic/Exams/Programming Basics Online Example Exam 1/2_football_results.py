wins = 0
losses = 0
draws = 0

for football_match in range(3):
    first_score, second_score = input().split(":")
    home_score = int(first_score)
    away_score = int(second_score)
    if home_score > away_score:
        wins += 1
    elif home_score < away_score:
        losses += 1
    elif home_score == away_score:
        draws += 1

print(f"Team won {wins} games.")
print(f"Team lost {losses} games.")
print(f"Drawn games: {draws}")