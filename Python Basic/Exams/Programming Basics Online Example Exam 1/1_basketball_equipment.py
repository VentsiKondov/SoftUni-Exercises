annual_tax = int(input())

basketball_shoes = annual_tax * 0.6
basketball_cloths = basketball_shoes * 0.8
basketball_ball = basketball_cloths / 4
basketball_accessories = basketball_ball / 5

total = annual_tax + basketball_ball + basketball_accessories + basketball_cloths + basketball_shoes
print(f'{total:.2f}')