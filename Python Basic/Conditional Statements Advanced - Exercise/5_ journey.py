budget = float(input())
season = input()

destination = ''
place_price = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place_price = budget * 0.3
    elif season == "winter":
        place_price = budget * 0.7
elif 100<budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place_price = budget * 0.4
    elif season == "winter":
        place_price = budget * 0.8
elif budget > 1000:
    destination = "Europe"
    place_price = 0.9 * budget

if season == "summer" and destination != 'Europe':
    print(f"Somewhere in {destination}")
    print(f"Camp - {place_price:.2f}")
elif season == "winter":
    print(f"Somewhere in {destination}")
    print(f"Hotel - {place_price:.2f}")
else:
    print(f"Somewhere in {destination}")
    print(f"Hotel - {place_price:.2f}")