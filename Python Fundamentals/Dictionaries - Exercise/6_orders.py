


my_dictionary = {}
while True:
    items = input().split()
    if items[0] == 'buy':
        break
    product, price, quantity = items
    quantity = float(quantity)
    price = float(price)
    if product not in my_dictionary:
        my_dictionary[product] = [price, quantity]
    elif product in my_dictionary:
        my_dictionary[product][0] = price
        my_dictionary[product][1] += quantity


for key, value in my_dictionary.items():
    print(f'{key} -> {value[0]*value[1]:.2f}')