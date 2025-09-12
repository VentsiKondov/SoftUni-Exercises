import math

people = int(input())
elevator_capacity = int(input())

print(math.ceil(people / elevator_capacity))


# courses = people // elevator_capacity
# people -= courses * elevator_capacity
#
# if people % elevator_capacity == 0:
#     print(courses)
# else:
#     print(courses + 1)