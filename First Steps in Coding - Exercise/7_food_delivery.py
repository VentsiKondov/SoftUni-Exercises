number_of_chicken_menus = int(input())
number_of_fish_menus = int(input())
number_of_vegetarian_menus = int(input())

all_sum = number_of_chicken_menus * 10.35 + number_of_fish_menus * 12.4 + number_of_vegetarian_menus * 8.15
dessert_price = all_sum * 0.2
total = all_sum + dessert_price + 2.5
print(total)