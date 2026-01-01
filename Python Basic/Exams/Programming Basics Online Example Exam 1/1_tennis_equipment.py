from math import floor, ceil

price_for_one_tennis_racquet = float(input())
number_of_tennis_racquets = int(input())
number_of_pairs = int(input())


price_for_one_pair = price_for_one_tennis_racquet / 6

total_price_pairs = number_of_pairs * price_for_one_pair
total_price_for_racquets = price_for_one_tennis_racquet * number_of_tennis_racquets

final_sum = total_price_pairs + total_price_for_racquets + ((total_price_pairs + total_price_for_racquets) * 0.2)
print(f"Price to be paid by Djokovic {floor(final_sum / 8)}")
print(f"Price to be paid by sponsors {ceil(final_sum * (7/8))}")