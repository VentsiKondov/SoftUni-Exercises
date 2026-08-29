days = int(input())
quantity_food = float(input())
cat_food_quantity = 0
dog_food_quantity = 0
biscuits = 0
for day in range(1,days+1):
    dog_eaten_food = int(input())
    cat_eaten_food = int(input())
    dog_food_quantity += dog_eaten_food
    cat_food_quantity += cat_eaten_food
    if day % 3 == 0:
        biscuits += (dog_eaten_food + cat_eaten_food) * 0.1
dog_and_cat_food = dog_food_quantity + cat_food_quantity
print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{(dog_and_cat_food/ quantity_food)*100:.2f}% of the food has been eaten.")
print(f"{(dog_food_quantity/dog_and_cat_food )*100:.2f}% eaten from the dog.")
print(f"{(cat_food_quantity/dog_and_cat_food)*100:.2f}% eaten from the cat.")
