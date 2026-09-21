numbers = list(map(int, input().split()))
execution_number = int(input())


new_list = []
pos = execution_number - 1
index = 0
while numbers:

    index = (pos+index) % len(numbers)
    new_list.append(numbers.pop(index))

print(f"[{''.join(str(c)for c in new_list)}]")

