

first_deque = {int(x) for x in input().split()}
second_deque = {int(x) for x in input().split()}


for _ in range(int(input())):
    command, *data = input().split()
    sequence = data.pop(0)
    full_command = command +" "+ sequence
    if command == "Add" and sequence == "First":
        for num in data:
            first_deque.add(int(num))


    elif command == "Add" and sequence == "Second":
        for num in data:
            second_deque.add(int(num))
    elif command == "Remove" and sequence == "First":
        for num in data:
            first_deque.discard(int(num))


    elif command == "Remove" and sequence == "Second":
        for num in data:
            second_deque.discard(int(num))


    else:
        if set(first_deque).issubset(set(second_deque)) or set(second_deque).issubset(set(first_deque)):
            print("True")
        else:
            print("False")


print(*sorted(first_deque), sep=", ")
print(*sorted(second_deque), sep=", ")


