player_goals = {}
best_goals = 0
best_player = None

while True:
    player = input()
    if player == "END":
        break
    goals = int(input())
    player_goals[player] = goals
    if goals >= 10:
        break


for player, goals in player_goals.items():
    if goals > best_goals:
        best_player = player
        best_goals = goals

print(f"{best_player} is the best player!")

if best_goals >= 3:
    print(f"He has scored {best_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_goals} goals.")

