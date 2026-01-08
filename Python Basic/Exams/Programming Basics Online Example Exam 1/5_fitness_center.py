people = int(input())
fitness_dict ={
    'Back': 0,
    'Chest': 0,
    'Legs': 0,
    'Abs': 0,
    'Protein shake': 0,
    'Protein bar': 0,
}
workout_people = 0
for _ in range(people):
    workout = input()
    if workout in fitness_dict:
        fitness_dict[workout] += 1



non_workout = fitness_dict['Protein shake'] + fitness_dict['Protein bar']

print(f"{fitness_dict['Back']} - back")
print(f"{fitness_dict['Chest']} - chest")
print(f"{fitness_dict['Legs']} - legs")
print(f"{fitness_dict['Abs']} - abs")
print(f"{fitness_dict['Protein shake']} - protein shake")
print(f"{fitness_dict['Protein bar']} - protein bar")

workout_people = people - non_workout

workout_percentage = workout_people/people * 100
non_workout_percentage = non_workout/people * 100

print(f'{workout_percentage:.2f}% - work out')
print(f'{non_workout_percentage:.2f}% - protein')
