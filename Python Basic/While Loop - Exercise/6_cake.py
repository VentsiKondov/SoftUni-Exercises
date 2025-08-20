length_cake = int(input()) * int(input())
while length_cake > 0:
    command = input()
    if command == 'STOP':
        print(f"{length_cake} pieces are left.")
        break
    current_piece = int(command)
    length_cake -= current_piece
else:
    print(f"No more cake left! You need {abs(length_cake)} pieces more.")