peters_budget = float(input())
number_video_cards = int(input())
number_processors = int(input())
number_ram = int(input())
video_card_price = 250 * number_video_cards


one_processors_price = 0.35 * video_card_price
processor_price = number_processors * one_processors_price


one_ram_price = 0.1 * video_card_price
ram_price = one_ram_price * number_ram

final_sum = ram_price + video_card_price + processor_price
if number_video_cards > number_processors:
    final_sum = final_sum - 0.15* final_sum
if final_sum > peters_budget:
    print(f"Not enough money! You need {abs(final_sum-peters_budget):.2f} leva more!")
else:
    print(f"You have {abs(final_sum-peters_budget):.2f} leva left!")