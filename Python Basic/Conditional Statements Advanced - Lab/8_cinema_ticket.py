day = input()
days_of_week = {
    "Monday": 12,
    "Tuesday": 12,
    "Wednesday": 14,
    "Thursday": 14,
    "Friday": 12,
    "Saturday": 16,
    "Sunday": 16,
}

print(days_of_week.get(day))