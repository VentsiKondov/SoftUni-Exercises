numbers = input().split("|")
num_lst = []
for n in numbers[::-1]:
    num_lst.extend(n.split())

print(*num_lst)

