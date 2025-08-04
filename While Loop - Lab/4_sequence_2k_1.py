max_num = int(input())
start = 1
print(start)
while start < max_num:

    start = start * 2 + 1
    if start > max_num:
        break
    print(start)
