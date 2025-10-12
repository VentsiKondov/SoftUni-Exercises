fire_cells = input().split("#")
effort = 0
total_effort = 0
total_fire = 0
water = int(input())
print("Cells:")
for cell in fire_cells:
    single_cell = cell.split(" = ")
    type_of_fire = single_cell[0]
    value = int(single_cell[1])
    effort = 0.25 * value
    if water >= value:
        if type_of_fire == "High" and 81 <=value <=125:
            water -= value
            total_effort += effort
            total_fire += value
            print(f"- {value}")
        elif type_of_fire == "Medium" and 51<=value <=80:
            water -= value
            total_effort += effort
            total_fire += value
            print(f"- {value}")
        elif type_of_fire == "Low" and 1<=value <=50:
            water -= value
            total_effort += effort
            total_fire += value
            print(f"- {value}")
print(f'Effort: {total_effort:.2f}')
print(f'Fire: {total_fire}')
