sequence = [int(s) for s in input().split()]
capacity = int(input())
capacity_copy = capacity
number_of_rows = 1
sequence_copy = sequence.copy()
while sequence_copy:
    cloth = sequence_copy[-1]
    if capacity_copy - cloth < 0:
        number_of_rows += 1
        capacity_copy = capacity

    else:
        capacity_copy -= cloth
        sequence_copy.pop()

print(number_of_rows)