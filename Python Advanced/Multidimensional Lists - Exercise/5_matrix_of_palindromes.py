rows ,cols = [int(x) for x in input().split()]

start = ord("a")
for i in range(rows):
    current_start = ord("a") + i
    new_lst = []
    for j in range(cols):
        result = chr(current_start) + chr(current_start + j) + chr(current_start)
        new_lst.append(result)

    print(*new_lst)