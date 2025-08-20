

product_name =input()
fruits = 'banana, apple, kiwi, cherry, lemon, grapes'
vegetables = 'tomato cucumber pepper carrot'
if product_name in fruits:
    print("fruit")
elif product_name in vegetables:
    print("vegetable")
else:
    print("unknown")