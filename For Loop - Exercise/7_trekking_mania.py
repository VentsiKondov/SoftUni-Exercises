number_of_groups = int(input())
musala = []
monblan = []
kilimanjaro = []
k2 = []
everest = []
all_people_sum = 0
for i in range(number_of_groups):
    people_per_group = int(input())
    if people_per_group <= 5:
        musala.append(people_per_group)
    elif 6<= people_per_group <= 12:
        monblan.append(people_per_group)
    elif 13 <= people_per_group <= 25:
        kilimanjaro.append(people_per_group)
    elif 26 <= people_per_group <= 40:
        k2.append(people_per_group)
    elif 41 <= people_per_group:
        everest.append(people_per_group)
    all_people_sum += people_per_group

print(f"{sum(musala) / all_people_sum * 100:.2f}%")
print(f"{sum(monblan) / all_people_sum * 100:.2f}%")
print(f"{sum(kilimanjaro) / all_people_sum * 100:.2f}%")
print(f"{sum(k2) / all_people_sum * 100:.2f}%")
print(f"{sum(everest) / all_people_sum * 100:.2f}%")
