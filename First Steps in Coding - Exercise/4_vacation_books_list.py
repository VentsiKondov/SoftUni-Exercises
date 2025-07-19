pages = int(input())
pages_per_hour = int(input())
days = int(input())

pages_hours = pages / pages_per_hour
time =round(pages_hours / days)
print(time)