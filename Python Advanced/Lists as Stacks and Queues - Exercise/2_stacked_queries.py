number_of_lines =int(input())
my_stack = []

for i in range(number_of_lines):
    query = input()
    if query.startswith("1"):
        com, number = query.split(" ")
        my_stack.append(int(number))
    elif query.startswith("2"):
        if my_stack:
            my_stack.pop()
    elif query.startswith("3"):
        if my_stack:
            print(max(my_stack))
    elif query.startswith("4"):
        if my_stack:
            print(min(my_stack))

print(', '.join(map(str,reversed(my_stack))))
