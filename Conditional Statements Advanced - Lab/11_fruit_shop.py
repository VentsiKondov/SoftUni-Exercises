working_days ={
    "banana": 2.5,
    "apple": 1.2,
    "orange": 0.85,
    "grapefruit": 1.45,
    "kiwi": 2.7,
    "pineapple": 5.5,
    "grapes": 3.85
}

weekend_days ={
    "banana": 2.7,
    "apple": 1.25,
    "orange": 0.9,
    "grapefruit": 1.6,
    "kiwi": 3,
    "pineapple": 5.6,
    "grapes": 4.2
}
product = input()
day =input()
quantity = float(input())
work_days = "Monday Tuesday Wednesday Thursday Friday"
weekend = "Saturday Sunday"
if day in work_days:
    result = working_days.get(product, "error")
    if result == "error":
        print(result)
    else:
        print(f"{result * quantity:.2f}")
elif day in weekend:
    result = weekend_days.get(product, "error")
    if result == "error":
        print(result)
    else:
        print(f"{result * quantity:.2f}")
else:
    print("error")