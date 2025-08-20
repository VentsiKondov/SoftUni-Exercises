first_player_seconds = int(input())
second_player_seconds = int(input())
third_player_seconds = int(input())

total_seconds = first_player_seconds + second_player_seconds + third_player_seconds
minutes = total_seconds // 60
seconds = total_seconds % 60
if seconds <10:
    seconds = "0" + str(seconds)

print(f"{minutes}:{seconds}")

