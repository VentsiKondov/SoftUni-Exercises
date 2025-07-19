deposit_sum = float(input())
time_for_the_deposit = int(input())
year_percent =float(input()) / 100

total_sum = deposit_sum + time_for_the_deposit *((deposit_sum * year_percent)/12)
print(total_sum)