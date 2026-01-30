n, m = input().split()
first_set = {int(input()) for _ in range(int(n))}
second_set = {int(input()) for _ in range(int(m))}
intersection = first_set.intersection(second_set)
for num in intersection:
    print(num)
