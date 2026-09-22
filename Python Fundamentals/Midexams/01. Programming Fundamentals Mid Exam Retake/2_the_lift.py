all_people = int(input())
wagons = list(map(int, input().split()))

max_capacity = 4
for wagon in range(len(wagons)):
    current_wagon = wagons[wagon]
    free_space = max_capacity - current_wagon
    if free_space <=0:
        continue
    take = min(free_space, all_people)
    wagons[wagon] += take
    all_people -= take
    if all_people == 0:
        break


if all_people == 0 and any(w < max_capacity for w in wagons):
    print('The lift has empty spots!')
    print(*wagons, sep=' ')
elif all_people > 0 and all(w == max_capacity for w in wagons):
    print(f"There isn't enough space! {all_people} people in a queue!")
    print(*wagons, sep=' ')
else:
    print(*wagons, sep=' ')



