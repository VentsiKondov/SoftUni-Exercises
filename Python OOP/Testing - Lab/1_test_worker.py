
class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'
import unittest
class WorkerTests(unittest.TestCase):
    def test_init(self):
        w = Worker('Gosho', 100,100)
        self.assertEqual(w.name, "Gosho")
        self.assertEqual(w.salary, 100)
        self.assertEqual(w.energy, 100)

    def test_rest_method(self):
        w = Worker('Gosho', 100,100)
        self.assertEqual(w.energy, 100)
        w.rest()
        self.assertEqual(w.energy, 101)
        w.rest()
        self.assertEqual(w.energy, 102)

    def test_invalid_energy_to_work(self):
        w = Worker('Gosho', 100,0)
        with self.assertRaises(Exception) as ex:
            w.work()
        self.assertEqual(str(ex.exception), "Not enough energy.")
        w.energy -= 1
        with self.assertRaises(Exception) as ex:
            w.work()
        self.assertEqual(str(ex.exception), "Not enough energy.")


    def test_valid_work_method(self):
        w = Worker('Gosho', 100,100)
        self.assertEqual(w.money, 0)
        self.assertEqual(w.energy, 100)
        w.work()
        self.assertEqual(w.money, 100)
        self.assertEqual(w.energy, 99)
        w.work()
        self.assertEqual(w.money, 200)
        self.assertEqual(w.energy, 98)

    def test_get_info(self):
        w = Worker('Gosho', 100,100)
        self.assertEqual(w.get_info(), f'{w.name} has saved {w.money} money.')



if __name__ == '__main__':
    unittest.main()
