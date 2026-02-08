materials = [int(x) for x in input().split()]
magic = [int(x) for x in input().split()]
task_tb_b = False
task_d_t = False
present = {150: ["Doll", 0],
           250: ["Wooden train", 0],
           300: ["Teddy bear", 0],
           400: ["Bicycle", 0],}


while magic and materials:
    current_material = materials[-1]
    current_magic = magic[0]
    total_magic = current_magic * current_material
    if total_magic in present.keys():
        present[total_magic][1] += 1
        materials.pop(-1)
        magic.pop(0)
    elif current_magic == 0 or total_magic == 0:
        if current_magic == 0:
            magic.pop(0)
        if current_material == 0:
            materials.pop(-1)
    elif total_magic not in present.keys() and total_magic > 0:
        magic.pop(0)
        materials.pop(-1)
        materials.append(current_material+15)
    if total_magic < 0:
        materials.pop(-1)
        magic.pop(0)
        sum_of_both = current_magic + current_material
        materials.append(sum_of_both)


if present[150][1] > 0 and present[250][1] > 0:
    task_d_t = True
    print("The presents are crafted! Merry Christmas!")
elif present[300][1] > 0 and present[400][1] > 0:
    task_tb_b = True
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")


if materials:
    print(f"Materials left: {', '.join(map(str, materials[::-1]))}")
if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

for present in sorted(present.values()):
    if present[1] > 0:
        print(f'{present[0]}: {present[1]}')










