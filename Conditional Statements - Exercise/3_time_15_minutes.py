hours = int(input())
minutes = int(input())

if minutes + 15 > 60:
    minutes = (minutes + 15) - 60
    hours += 1
    if minutes < 10:
        minutes = "0" + str(minutes)
elif minutes + 15 == 60:
    minutes = "00"
    hours += 1
    if hours == 24:
        hours = 0
else:
    minutes += 15
if hours == 24:
    hours = 0

print(f"{hours}:{minutes}")