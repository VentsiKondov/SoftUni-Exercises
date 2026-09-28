energy = int(input())
command = input()
out_of_energy = False
battles_won = 0


while command != 'End of battle':
    enemy_distance=  int(command)
    if enemy_distance > energy:
        out_of_energy = True
        break
    energy -= enemy_distance
    battles_won += 1
    if battles_won % 3 == 0:
        energy += battles_won
    command = input()

if out_of_energy:
    print(f'Not enough energy! Game ends with {battles_won} won battles and {energy} energy')
else:
    print(f"Won battles: {battles_won}. Energy left: {energy}")