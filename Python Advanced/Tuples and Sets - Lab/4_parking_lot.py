number_of_lines = int(input())
car_number_lst = []
for _ in range(number_of_lines):
    direction,car_number = input().split(", ")
    if direction == "IN":
        car_number_lst.append(car_number)
    elif direction == "OUT":
        if car_number in car_number_lst:
            car_number_lst.remove(car_number)

unique_names = set(car_number_lst)
if unique_names:
    [print(car_number) for car_number in unique_names]
else:
    print("Parking Lot is Empty")