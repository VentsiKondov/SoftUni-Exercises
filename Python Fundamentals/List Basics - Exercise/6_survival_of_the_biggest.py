old_list = list(map(int, input().split()))
number_to_remove = int(input())
new_list = sorted(old_list)
num = 0
print(new_list)
for i in range(0, number_to_remove):
    old_list.remove(new_list[i])
    print(new_list[i])
print(old_list)



# numbers = list(map(int, input().strip().split(" ")))
# [numbers.remove(min(numbers)) for _ in range(int(input()))]
# print(", ".join(str(x) for x in numbers))