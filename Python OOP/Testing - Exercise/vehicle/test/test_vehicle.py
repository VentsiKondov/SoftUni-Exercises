from artifacts.vehicle import Vehicle
import unittest

class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(20.5, 175.5)

    def test_constant(self):
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)

    def test_init(self):
        self.assertEqual(self.vehicle.fuel, 20.5)
        self.assertEqual(self.vehicle.capacity , self.vehicle.fuel)
        self.assertEqual(self.vehicle.horse_power, 175.5)
        self.assertEqual(self.vehicle.fuel_consumption , Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_method_without_needed_fuel(self):
        self.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1000)
        self.assertEqual(str(ex.exception), 'Not enough fuel')

    def test_drive_method_with_needed_fuel(self):
        self.vehicle.drive(4)
        self.assertEqual(self.vehicle.fuel, 15.5)

    def test_refuel_method_without_needed_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual(str(ex.exception), 'Too much fuel')

    def test_refuel_method_with_needed_fuel(self):
        self.vehicle.fuel = 1
        self.vehicle.refuel(1)
        self.assertEqual(self.vehicle.fuel, 2)

    def test_str_method(self):
        self.assertEqual(str(self.vehicle), f"The vehicle has 175.5 " +
               f"horse power with 20.5 fuel left and 1.25 fuel consumption")


if __name__ == '__main__':
    unittest.main()