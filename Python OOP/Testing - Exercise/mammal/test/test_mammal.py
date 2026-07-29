import unittest
from artifacts.mammal import Mammal

class MammalTest(unittest.TestCase):
    def setUp(self):
        self.Mammal = Mammal('Mammal', 'type mammal', 'sound')

    def test_if_all_data_is_correct(self):
        self.assertEqual(self.Mammal.name, 'Mammal')
        self.assertEqual(self.Mammal.sound, 'sound')
        self.assertEqual(self.Mammal.type, 'type mammal')
        #__init__

    def test_if_make_sound_is_correct(self):
        self.assertEqual(self.Mammal.make_sound(), 'Mammal makes sound')

    def test_if_get_kingdom_is_correct(self):
        self.assertEqual(self.Mammal.get_kingdom(), 'animals')

    def test_get_info_method(self):
        self.assertEqual(self.Mammal.info(), 'Mammal is of type type mammal')

if __name__ == '__main__':
    unittest.main()