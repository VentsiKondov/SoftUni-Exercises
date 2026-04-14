from project.drink import \
    Drink
from project.food import \
    Food
from project.product import Product

class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name:str):
        return next((p for p in self.products if p.name == product_name), None)

    def remove(self, product_name:str):
        product = self.find(product_name)

        if product:
            self.products.remove(product)

    def __repr__(self):
        result = [f'{p.name}: {p.quantity}' for p in self.products]
        return "\n".join(result)



