number_of_rows = int(input())
my_dictionary = {}
for i in range(number_of_rows):
    name = input()
    grade = float(input())
    if name not in my_dictionary:
        my_dictionary[name] = []
        my_dictionary[name].append(grade)
    else:
        my_dictionary[name].append(grade)


for name, grades in my_dictionary.items():
    average = sum(grades) / len(grades)
    if not 4.5<=average <= 6:
        continue
    print(f"{name} -> {average:.2f}")








