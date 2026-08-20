strawberry_price = float(input())

quantity_bananas = float(input())
quantity_oranges = float(input())
quantity_raspberry = float(input())
quantity_strawberry = float(input())


price_raspberry = strawberry_price / 2
price_oranges = price_raspberry - (0.4 * price_raspberry)
price_bananas = price_raspberry - (0.8 * price_raspberry)

straw_berry_final_price = strawberry_price * quantity_strawberry
raspberry_final_price = quantity_raspberry * price_raspberry
banana_final_price = price_bananas * quantity_bananas
orange_final_price = price_oranges * quantity_oranges

total_sum = straw_berry_final_price + banana_final_price + orange_final_price + raspberry_final_price
print(f'{total_sum:.2f}')
