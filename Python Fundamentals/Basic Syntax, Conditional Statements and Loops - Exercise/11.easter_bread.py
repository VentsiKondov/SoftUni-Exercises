budget = float(input())
price_for_one_kg_flour = float(input())
one_pack_of_eggs = 0.75 * price_for_one_kg_flour
milk_for_one_bread = (0.25 * price_for_one_kg_flour + price_for_one_kg_flour)/ 4
bread_count = 0
color_eggs = 0
while budget > 0:
    budget -=(price_for_one_kg_flour + one_pack_of_eggs + milk_for_one_bread)
    bread_count = bread_count + 1
    color_eggs = color_eggs + 3
    if bread_count % 3 == 0:
        color_eggs =  color_eggs - (bread_count - 2)
    if budget -(price_for_one_kg_flour + one_pack_of_eggs + milk_for_one_bread) < 0:
        print(f"You made {bread_count} loaves of Easter bread! Now you have {color_eggs} eggs and {budget:.2f}BGN left.")
        break


