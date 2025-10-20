number_of_rooms = int(input())
needed_chair = 0
free_chair = 0
game_on = False

for room in range(1, number_of_rooms+1):
    chairs_with_visitors = input().split()
    chairs = chairs_with_visitors[0]
    visitors = int(chairs_with_visitors[1])
    needed_chair = 0
    if visitors - len(chairs) < 0:
        free_chair += abs(visitors - len(chairs))
    elif visitors - len(chairs) > 0:
        needed_chair += abs(visitors - len(chairs))
        print(f'{needed_chair} more chairs needed in room {room}')
    else:
        game_on = True
if game_on:
     print(f"Game on,{free_chair} free chairs left ")
