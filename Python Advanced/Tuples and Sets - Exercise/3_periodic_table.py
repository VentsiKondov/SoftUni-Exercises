number_of_lines = int(input())
periodic_table = set()
for i in range(number_of_lines):
    chemical, *data = input().split()
    periodic_table.add(chemical)
    for el in data:
        periodic_table.add(el)

for chemical in periodic_table:
    print(chemical)