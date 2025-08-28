command = input()
coffee_needed = 0
while command != "END":
    if command == "coding" or command == "dog" or command == "cat" or command == "movie" and command == command.lower():
        coffee_needed += 1
    if command == command.upper():
        coffee_needed += 2
    command = input()
if coffee_needed > 5:
    print("You need extra sleep")
else:
    print(coffee_needed)
