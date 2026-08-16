from math import floor
def calculation(c, p):
    if c == "black":
        return "divide"

    elif c in colors_with_points:
        p += colors_with_points[c][0]
        colors_with_points[c][1] += 1
    else:
        return "other"
    return p





colors_with_points = {
    "red": [5, 0],
    "orange": [10, 0],
    "yellow": [15, 0],
    "white": [20, 0],
    "black": [0],
    "other": [0],
}

number_of_balls = int(input())
points = 0
for _ in range(number_of_balls):
    color = input()
    command = calculation(color, points)
    if command == "divide":
        points = floor(points/2)
        colors_with_points[color][0] += 1
        continue
    elif command == "other":
        colors_with_points["other"][0] += 1
        continue
    points = int(command)

output = [
    f"Total points: {points}",
    f"Red balls: {colors_with_points['red'][1]}",
    f"Orange balls: {colors_with_points['orange'][1]}",
    f"Yellow balls: {colors_with_points['yellow'][1]}",
    f"White balls: {colors_with_points['white'][1]}",
    f"Other colors picked: {colors_with_points['other'][0]}",
    f"Divides from black balls: {colors_with_points['black'][0]}",
]

for line in output:
    print(line)