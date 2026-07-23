class Cat:

  def __init__(self, name):
    self.name = name
    self.fed = False
    self.sleepy = False
    self.size = 0

  def eat(self):
    if self.fed:
      raise Exception('Already fed.')

    self.fed = True
    self.sleepy = True
    self.size += 1

  def sleep(self):
    if not self.fed:
      raise Exception('Cannot sleep while hungry')

    self.sleepy = False

import unittest
class CatTests(unittest.TestCase):
    def test_eat_method(self):
        c = Cat("Cat")
        self.assertEqual(c.fed, False)
        self.assertEqual(c.size, 0)
        c.eat()
        self.assertEqual(c.fed, True)
        self.assertEqual(c.size, 1)
        self.assertEqual(c.sleepy, True)
        with self.assertRaises(Exception) as ex:
            c.eat()
        self.assertEqual(str(ex.exception),'Already fed.')

    def test_sleep_method(self):
        c = Cat("Cat")
        with self.assertRaises(Exception) as ex:
            c.sleep()
        self.assertEqual(str(ex.exception),'Cannot sleep while hungry')
        c.eat()
        self.assertEqual(c.fed, True)
        self.assertEqual(c.sleepy, True)
        c.sleep()
        self.assertEqual(c.sleepy, False)

if __name__ == '__main__':
    unittest.main()