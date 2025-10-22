lst_with_numbers = list(map(int, input().split(", ")))
for n in range(1, 11):
    new_list = []
    if len(lst_with_numbers) !=0:
        [new_list.append(i) for i in lst_with_numbers if i <= n *10]
        [lst_with_numbers.remove(o) for o in new_list]
        print(f"Group of {n * 10}'s: {new_list}")