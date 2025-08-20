free_space = int(input()) * int(input()) * int(input())
command = input()
while command != "Done":
    number_of_boxes = int(command)
    free_space -= number_of_boxes
    if free_space < 0:
        print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
        break
    command = input()
else:
    print(f"{free_space} Cubic meters left.")
