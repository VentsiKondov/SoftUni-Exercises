lost_fights = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

is_helmet_broken = False
shield_break_counter = 0
money = 0

for lost_fight in range(1, lost_fights+1):
    is_helmet_broken = False
    if lost_fight % 2 == 0:
        is_helmet_broken = True
        money += helmet_price

    if lost_fight % 3 == 0:
        money += sword_price
        if is_helmet_broken:
            money += shield_price
            shield_break_counter += 1
            if shield_break_counter % 2 ==0:
                money += armor_price

print(f"Gladiator expenses: {money:.2f} aureus")

