from collections import \
    deque

quantity_of_water = int(input())
command = input()
people = deque()
while command != 'Start':
    name = command
    people.append(name)
    command = input()

while True:
    line = input()
    if line == 'End':
        break
    current_command = line.split()
    if len(current_command) == 2:
        quantity_of_water += int(current_command[1])
    else:
        current_person = people.popleft()
        water_needed = int(current_command[0])
        if quantity_of_water >= water_needed:
            print(f"{current_person} got water")
            quantity_of_water -= water_needed
        else:
            print(f"{current_person} must wait" )
print(f"{quantity_of_water} liters left")