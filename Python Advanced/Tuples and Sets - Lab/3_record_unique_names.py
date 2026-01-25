lst_with_names = [input() for _ in range(int(input()))]
unique_names = set(lst_with_names)
for name in unique_names:
    print(name)