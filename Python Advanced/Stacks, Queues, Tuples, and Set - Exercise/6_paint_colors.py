words = [word for word in input().split()]
main_colors = ["red", "yellow", "blue", "orange", "green", "purple"]
secondary_colors = {"orange": ["red","yellow"],
                    "purple": ["red","blue"],
                    "green": ["yellow","blue"],}

new_colors = []
while words:
    first_char = words.pop(0)
    last_char = words.pop(-1) if words else ""
    middle = len(words) // 2
    for color in (first_char + last_char, last_char + first_char):
        if color in main_colors:
            new_colors.append(color)
            break
    else:
        for el in (first_char[:-1], last_char[:-1]):
            if el:
                words.insert(middle, el)

for color, required_colors in secondary_colors.items():
    if color in new_colors:
        if required_colors[0] not in new_colors or required_colors[1] not in new_colors:
            new_colors.remove(color)


print(new_colors)


