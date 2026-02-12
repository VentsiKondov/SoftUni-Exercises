rows = int(input())
res = []

for i in range(rows):
    res += [int(x) for x in input().split(', ')]
print(res)