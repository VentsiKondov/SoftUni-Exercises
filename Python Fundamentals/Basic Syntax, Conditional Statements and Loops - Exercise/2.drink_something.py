person_age = int(input())
if person_age <= 14 and person_age > 0:
    print("drink toddy")
elif person_age > 14 and person_age <= 18:
    print("drink coke")
elif person_age <= 21 and person_age > 18:
    print("drink beer")
elif person_age > 21:
    print("drink whisky")
