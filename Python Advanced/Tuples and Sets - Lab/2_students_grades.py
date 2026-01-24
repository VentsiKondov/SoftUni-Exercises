number_of_students = int(input())

grade_book = {}

for _ in range(number_of_students):
    student_name, grade = input().split()
    if student_name in grade_book:
        grade_book[student_name].append(float(grade))
    else:
        grade_book[student_name] = [float(grade)]

for name,grades in grade_book.items():
    average = sum(grades) / len(grades)
    print(f"{name} -> {' '.join([f'{el:.2f}' for el in grades])} (avg: {average:.2f})")