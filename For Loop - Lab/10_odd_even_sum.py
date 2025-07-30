sum_odd = 0
sum_even = 0

for num in range(int(input())):
    current_number = int(input())
    if num % 2 == 0:
        sum_even += current_number
    else:
        sum_odd += current_number

if sum_odd == sum_even:
    print("Yes")
    print(f"Sum = {sum_odd}")
else:
    print(f"No")
    print(f"Diff = {abs(sum_odd - sum_even)}")
