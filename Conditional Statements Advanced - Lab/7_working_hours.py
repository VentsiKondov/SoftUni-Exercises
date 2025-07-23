time = int(input())
day =input()
possible_days ="Monday Tuesday Wednesday Thursday Friday Saturday"
if day in possible_days and time in range(10, 19):
    print("open")
else:
    print("closed")
