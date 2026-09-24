first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
student_count = int(input())
hours = 0


total_eff = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
while student_count > 0:
    student_count -= total_eff
    hours += 1
    if hours % 4 ==0:
        hours += 1

print(f'Time needed: {hours}h.')
