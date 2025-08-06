number_of_unwanted_grades = int(input())
counter = 0
grades = []
last_exercise = None
exercise_counter = 0
while True:
    name_of_exercise = input()

    if name_of_exercise == "Enough":
        average = sum(grades) / len(grades)
        print(f"Average score: {average:.2f}")
        print(f"Number of problems: {exercise_counter}")
        print(f"Last problem: {last_exercise}")
        break

    grade = int(input())
    if grade <= 4:
        counter += 1
        if counter == number_of_unwanted_grades:
            print(f"You need a break, {number_of_unwanted_grades} poor grades.")
            break

    exercise_counter += 1
    grades.append(grade)
    last_exercise = name_of_exercise

