player_first = input()
player_second = input()
first_player_points = 0
second_player_points = 0
number_wars = False

def points_calculator(first, second, first_points, second_points):
    if first > second:
        first_points += first - second
    elif first_player_card < second_player_card:
        second_points += second - first
    else:
        return "Number Wars"
    return first_points, second_points


while True:
    command = input()
    if command == 'End of game':
        break
    first_player_card = int(command) # 2-9
    second_player_card = int(input())# 2-9
    if not points_calculator(first_player_card,second_player_card,first_player_points,second_player_points) == "Number Wars":
        first_player_points ,second_player_points = points_calculator(first_player_card,second_player_card,first_player_points,second_player_points)
    else:
        print("Number wars!")
        first_bonus_card = int(input())
        second_bonus_card = int(input())
        number_wars = True
        if first_bonus_card > second_bonus_card:
            print(f"{player_first} is winner with {first_player_points} points")
            break
        elif first_bonus_card < second_bonus_card:
            print(f"{player_second} is winner with {second_player_points} points")
            break



if not number_wars:
    print(f"{player_first} has {first_player_points} points")
    print(f"{player_second} has {second_player_points} points")