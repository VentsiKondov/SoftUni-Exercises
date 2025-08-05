name = input()
is_not_graduated = False
counter = 0
bad_years =0
lst_with_grade = []
while counter < 12:
    grade = float(input())
    if grade < 4:
        bad_years += 1
        if bad_years == 2:
            print(f'{name} has been excluded at {counter + 1} grade')
            break
        continue
    lst_with_grade.append(grade)
    counter += 1
else:
    average_grade =  sum(lst_with_grade) / len(lst_with_grade)
    print(f'{name} graduated. Average grade: {average_grade:.2f}')

