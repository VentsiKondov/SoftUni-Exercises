class PizzaDelivery:
    def __init__(self, name:str, price:float, ingredients:dict):
        self.name = name
        self.price = float(price)
        self.ingredients = ingredients
        self.ordered = False


    def add_extra(self, ingredient:str, quantity:int, price_per_quantity:float):
        if not self.ordered:
            self.ingredients[ingredient] = self.ingredients.get(ingredient, 0) + quantity
            self.price  += price_per_quantity * quantity
        return f"Pizza {self.name} already prepared, and we can't make any changes!"


    def remove_ingredient(self, ingredient:str, quantity:int, price_per_quantity:float) -> (str, None):
        if not self.ordered:
            if ingredient not in self.ingredients.keys():

                return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

            if  quantity > self.ingredients[ingredient]:
                return f"Please check again the desired quantity of {ingredient}!"


            self.ingredients[ingredient] -= quantity
            self.price -= quantity * price_per_quantity
        return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def make_order(self):
        self.ordered = True
        if self.ordered:
            result = ", ".join(f'{k}: {v}' for k, v in self.ingredients.items())
            return f"You've ordered pizza {self.name} prepared with {result} and the price will be {int(self.price)}lv."
        return f"Pizza {self.name} already prepared, and we can't make any changes!"


