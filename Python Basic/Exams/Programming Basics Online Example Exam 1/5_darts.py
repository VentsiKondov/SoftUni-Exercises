player_name = input()
good_shots = 0
bad_shots = 0
STARTING_POINTS = 301
is_retired = False


def str_to_num(multiplier):
    if multiplier == "Single":
        return 1
    elif multiplier == "Double":
        return 2
    elif multiplier == "Triple":
        return 3


while True:
    command = input()
    if command == "Retire":
        is_retired = True
        break


    multiplier = command
    points = int(input())
    multiplier = str_to_num(multiplier)
    total_points = points * multiplier


    if total_points > STARTING_POINTS:
        bad_shots += 1
        continue
    elif total_points <= STARTING_POINTS:
        if STARTING_POINTS - total_points > 0:
            STARTING_POINTS -= total_points
            good_shots += 1
        elif STARTING_POINTS - total_points == 0:
            STARTING_POINTS -= STARTING_POINTS - total_points
            good_shots += 1
            break

if is_retired:
    print(f"{player_name} retired after {bad_shots} unsuccessful shots.")
else:
    print(f"{player_name} won the leg with {good_shots} shots.")