from collections import \
    deque

working_bees = deque([int(x) for x in input().split()])
nectar = deque([int(x) for x in input().split()])
symbols = deque([x for x in input().split()])
total_honey = 0

my_dict = {"*": lambda a,b:  int(a) * int(b),
           "+": lambda a,b:  int(a) + int(b),
           "-": lambda a,b:  int(a) - int(b),
           "/": lambda a,b:  int(a) / int(b)}



while working_bees and nectar:
    first_bee = working_bees.popleft()
    last_nectar = nectar.pop()
    if last_nectar < first_bee:
        working_bees.appendleft(first_bee)
        continue
    current_symbol = symbols.popleft()
    if last_nectar == 0 and current_symbol == "/":
        continue
    total_honey += abs(my_dict[current_symbol](first_bee, last_nectar))


print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join(map(str, list(working_bees)))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, list(nectar)))}")