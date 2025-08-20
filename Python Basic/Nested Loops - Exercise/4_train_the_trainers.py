judges = int(input())


average_lst = []
while True:
    command = input()
    if command == "Finish":
        break

    title = command
    grade_counter = 0
    sum_grade = 0
    for judge in range(judges):
        grade = float(input())
        sum_grade += grade
        grade_counter += 1

    average = sum_grade / grade_counter
    average_lst.append(average)
    print(f"{title} - {average:.2f}.")

print(f"Student's final assessment is {sum(average_lst)/ len(average_lst):.2f}.")
