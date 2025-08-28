command = input()
is_closed =False
while command != "Welcome!":
    if command == "Voldemort":
        is_closed = True
        break
    if len(command) == 5:
        print(f"{command} goes to Slytherin.")
    elif len(command) < 5 :
        print(f"{command} goes to Gryffindor.")
    elif len(command) == 6:
        print(f"{command} goes to Ravenclaw.")
    else:
        print(f"{command} goes to Hufflepuff.")
    command = input()

if is_closed:
    print("You must not speak of that name!")
else:
    print("Welcome to Hogwarts.")