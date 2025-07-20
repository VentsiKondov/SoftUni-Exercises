number_of_pens = int(input())
number_of_markers = int(input())
litres_for_cleaning = int(input())
percent_discount = int(input()) / 100

all_sum = number_of_pens * 5.8 + number_of_markers * 7.2 + litres_for_cleaning * 1.2
total_sum = all_sum - all_sum * percent_discount
print(total_sum)
