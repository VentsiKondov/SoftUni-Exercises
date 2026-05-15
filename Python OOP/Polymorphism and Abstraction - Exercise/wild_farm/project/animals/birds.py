from project.animals.animal import \
    Animal, \
    Bird
from project.food import \
    Vegetable, \
    Fruit, \
    Meat, \
    Seed


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    @property
    def gained_weight(self):
        return 0.25

    @property
    def food_that_eat(self):
        return [Meat]

class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
    @staticmethod
    def make_sound():
        return "Cluck"

    @property
    def food_that_eat(self):
        return [Vegetable, Fruit, Meat, Seed]

    @property
    def gained_weight(self):
        return 0.35

