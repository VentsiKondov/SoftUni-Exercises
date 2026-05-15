from project.animals.animal import \
    Mammal
from project.food import \
    Meat, \
    Vegetable, \
    Fruit


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Squeak"

    @property
    def food_that_eat(self):
        return [Fruit, Vegetable]

    @property
    def gained_weight(self):
        return 0.1

class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
    @staticmethod
    def make_sound():
        return "Woof!"

    @property
    def food_that_eat(self):
        return [Meat]
    @property
    def gained_weight(self):
        return 0.40

class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
    @staticmethod
    def make_sound():
        return "Meow"

    @property
    def food_that_eat(self):
        return [Meat, Vegetable]

    @property
    def gained_weight(self):
        return 0.3

class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
    @staticmethod
    def make_sound():
        return "ROAR!!!"

    @property
    def food_that_eat(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 1