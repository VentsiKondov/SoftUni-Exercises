team_a = ["A-1", "A-2", "A-3" , "A-4" , "A-5" , "A-6" , "A-7" , "A-8" , "A-9", "A-10", "A-11"]
team_b = ["A-1", "A-2", "A-3" , "A-4" , "A-5" , "A-6" , "A-7" , "A-8" , "A-9", "A-10", "A-11"]
cards = input().split()
is_terminated = False

for card in cards:
    if len(team_a) < 7 or len(team_b) < 7:
        is_terminated = True
        break
    if card in team_a:
        team_a.remove(card)
    elif card in team_b:
        team_b.remove(card)


if is_terminated:
    print("Game was terminated")
    print(f"Team A: {len(team_a)}")
    print(f"Team B: {len(team_b)}")

else:
    print(f"Team A: {len(team_a)}")
    print(f"Team B: {len(team_b)}")