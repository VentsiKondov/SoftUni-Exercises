country = input()
equipment = input()
difficulty = 0
performance = 0

if country == 'Russia':
    if equipment == 'ribbon':
        difficulty = 9.1
        performance = 9.4
    elif equipment == 'hoop':
        difficulty = 9.3
        performance = 9.8
    elif equipment == 'rope':
        difficulty = 9.6
        performance = 9.0
elif country == 'Bulgaria':
    if equipment == 'ribbon':
        difficulty = 9.6
        performance = 9.4
    elif equipment == 'hoop':
        difficulty = 9.550
        performance = 9.750
    elif equipment == 'rope':
        difficulty = 9.500
        performance = 9.400
elif country == 'Italy':
    if equipment == 'ribbon':
        difficulty = 9.2
        performance = 9.5
    elif equipment == 'hoop':
        difficulty = 9.45
        performance = 9.35
    elif equipment == 'rope':
        difficulty = 9.70
        performance = 9.150

final = difficulty + performance
points_left = 20 - final
percentage_left = (points_left/20) * 100
print(f"The team of {country} get {final:.3f} on {equipment}.")
print(f"{percentage_left:.2f}%")