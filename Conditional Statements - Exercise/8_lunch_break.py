import math
serial_name = input()
time_one_episode = int(input())
break_time = int(input())

lunch_break = 1/8 * break_time
normal_break = 1/4 * break_time
break_time -= lunch_break + normal_break
if break_time >= time_one_episode:
    print(f"You have enough time to watch {serial_name} and left with {math.ceil(abs(break_time- time_one_episode))} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {math.ceil(abs(break_time-time_one_episode))} more minutes.")