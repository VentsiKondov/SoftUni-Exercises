STEPS_PER_DAY = 10000
total_steps =0
while total_steps < STEPS_PER_DAY:
    command = input()
    if command == "Going home":
        total_steps += int(input())
        if total_steps < STEPS_PER_DAY:
            print(f"{STEPS_PER_DAY - total_steps} more steps to reach goal.")
            break
        else:
            print(f'Goal reached! Good job!')
            print(f"{total_steps - STEPS_PER_DAY} steps over the goal!")
            break
    current_steps = int(command)
    total_steps += current_steps
else:
    print(f'Goal reached! Good job!')
    print(f"{total_steps - STEPS_PER_DAY} steps over the goal!")



