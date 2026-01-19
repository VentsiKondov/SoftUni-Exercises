
from collections import deque

quantity_of_food_for_the_day = int(input())
is_not_enough =False

quantity_of_food_deque = deque(map(int, input().split()))
print(max(quantity_of_food_deque))
while len(quantity_of_food_deque):
    order = quantity_of_food_deque[0]
    if order <= quantity_of_food_for_the_day:
        quantity_of_food_deque.popleft()
        quantity_of_food_for_the_day -= order
    else:
        is_not_enough = True
        break

if is_not_enough:
    print(f"Orders left: {' '.join(map(str, quantity_of_food_deque))}")
else:
    print(f"Orders complete")
