class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed




import unittest
class CarTests(unittest.TestCase):
    def test_init(self):
        c = Car("a", "b", 1, 4)
        self.assertEqual(c.make, "a")
        self.assertEqual(c.model, "b")
        self.assertEqual(c.fuel_consumption, 1)
        self.assertEqual(c.fuel_capacity, 4)
        self.assertEqual(c.fuel_amount, 0)

    def test_init_invalid_make(self):
        with self.assertRaises(Exception) as ex:
            Car("", "b", 1, 4)
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_init_invalid_model(self):
        with self.assertRaises(Exception) as ex:
            Car("a", "", 1, 4)
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_init_invalid_fuel_consumption(self):
        with self.assertRaises(Exception) as ex:
            Car("a", "b", 0, 4)
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")
    def test_init_invalid_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            Car("a", "b", 1, 0)
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")
    def test_init_invalid_fuel_amount(self):
        c=Car("a", "b", 10, 10)
        with self.assertRaises(Exception) as ex:
            c.fuel_amount = -1

        self.assertEqual(str(ex.exception), "Fuel amount cannot be negative!")

    def test_refuel_invalid_fuel(self):
        c = Car("a", "b", 1, 4)
        with self.assertRaises(Exception) as ex:
            c.refuel(0)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_valid_fuel(self):
        c = Car("a", "b", 1, 4)
        c.refuel(1)
        self.assertEqual(c.fuel_amount, 1)
        c.refuel(4)
        self.assertEqual(c.fuel_amount, 4)

    def test_drive_exception(self):
        c = Car("a", "b", 1, 4)
        with self.assertRaises(Exception) as ex:
            c.drive(105)
        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")

    def test_drive_valid(self):
        c = Car("a", "b", 1, 40)
        c.refuel(10)
        c.drive(10)
        self.assertEqual(c.fuel_amount, 9.9)


if __name__ == "__main__":
    unittest.main()

