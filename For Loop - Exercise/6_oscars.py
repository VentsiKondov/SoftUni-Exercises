actor_name = input()
points = float(input())
number_of_judges = int(input())

final_points = points
max_points = 1250.5

for _ in range(0, number_of_judges):
    name_of_judge = input()
    judge_points = float(input())
    final_points +=((len(name_of_judge) * judge_points) / 2)

    if final_points > max_points:
       print(f"Congratulations, {actor_name} got a nominee for leading role with {final_points:.1f}!")
       break
else:
    final_points = max_points - final_points
    print(f"Sorry, {actor_name} you need {final_points:.1f} more!")