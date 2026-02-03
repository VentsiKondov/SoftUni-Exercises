number_of_lines =int(input())
longest_intersection = {}
for _ in range(number_of_lines):
    first_list, second_list = [el.split(",") for el in input().split("-")]

    first_set = set(range(int(first_list[0]), int(first_list[1])+ 1))
    second_set = set(range(int(second_list[0]), int(second_list[1])+ 1))

    if len(first_set.intersection(second_set)) > len(longest_intersection):
        longest_intersection = first_set.intersection(second_set)


print(f"Longest intersection is {sorted(longest_intersection)} with length {len(longest_intersection)}")



