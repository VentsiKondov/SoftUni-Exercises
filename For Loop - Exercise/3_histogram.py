p1 = []
p2 = []
p3 = []
p4 = []
p5 = []
range_of_numbers = int(input())
for i in range(range_of_numbers):
    current_num = int(input())
    if current_num < 200:
        p1.append(current_num)
    elif 200<=current_num <= 399:
        p2.append(current_num)
    elif 400<=current_num<=599:
        p3.append(current_num)
    elif 600<=current_num<=799:
        p4.append(current_num)
    elif current_num >= 800:
        p5.append(current_num)

print(f"{len(p1) / range_of_numbers * 100:.2f}%")
print(f"{len(p2) / range_of_numbers * 100:.2f}%")
print(f"{len(p3) / range_of_numbers * 100:.2f}%")
print(f"{len(p4) / range_of_numbers * 100:.2f}%")
print(f"{len(p5) / range_of_numbers * 100:.2f}%")