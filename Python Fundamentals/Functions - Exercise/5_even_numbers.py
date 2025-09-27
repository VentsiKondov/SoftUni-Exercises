def even_numbers(lst):
    even_list = []
    for num in lst:
        if num % 2 == 0:
            even_list.append(num)
    return even_list



lst_of_num = list(map(int, input().split()))
even_list = even_numbers(lst_of_num)
print(even_list)
# print(list(filter(lambda num: num % 2 == 0, list(map(int, input().split())))))
