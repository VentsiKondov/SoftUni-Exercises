import math
pi = math.pi
shape = input()
if shape == "rectangle":
    side = float(input())
    side2 = float(input())
    face = side * side2
elif shape == "circle":
    side = float(input())
    face = pi * side ** 2
elif shape == "square":
    side = float(input())
    face = side * side
elif shape == "triangle":
    side = float(input())
    side2 = float(input())
    face = (side2 * side) / 2

print(f"{face:.3f}")