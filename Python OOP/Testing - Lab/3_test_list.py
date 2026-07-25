class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)

import unittest
class IntegerListTests(unittest.TestCase):
    def test_valid_init(self):
        i = IntegerList(1,2,3)
        self.assertEqual(i.get_data(), [1,2,3])
    def test_invalid_init(self):
        i = IntegerList(1,2,"a")
        self.assertEqual(i.get_data(), [1,2])

    def test_add(self):
        i = IntegerList(1,2,3)
        self.assertEqual(i.add(1), [1,2,3,1])
        self.assertEqual(i.add(2), [1,2,3,1,2])
        with self.assertRaises(ValueError) as ex:
            i.add("a")
        self.assertEqual(str(ex.exception), "Element is not Integer")

        with self.assertRaises(ValueError) as ex:
            i.add(1.5)
        self.assertEqual(str(ex.exception), "Element is not Integer")

    def test_biggest(self):
        i = IntegerList(1,2,3)
        self.assertEqual(i.get_biggest(), 3)

    def test_get_index(self):
        i = IntegerList(1,2,3)
        self.assertEqual(i.get_index(1), 0)

    def test_insert(self):
        i = IntegerList(1,2,3)
        with self.assertRaises(IndexError) as ex:
            i.insert(4,2)
        self.assertEqual(str(ex.exception), "Index is out of range")
        with self.assertRaises(IndexError) as ex:
            i.insert(3,2)
        self.assertEqual(str(ex.exception), "Index is out of range")
        with self.assertRaises(ValueError) as ex:
            i.insert(0,'a')
        self.assertEqual(str(ex.exception), "Element is not Integer")
        i.insert(0,1)
        self.assertEqual(i.get_data(), [1,1,2,3])

    def test_get_invalid(self):
        i = IntegerList(1,2,3)
        with self.assertRaises(IndexError) as ex:
            i.get(3)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_get_valid(self):
        i = IntegerList(1,2,3)
        self.assertEqual(i.get(0), 1)

    def test_remove_index_error(self):
        i = IntegerList(1,2,3)
        with self.assertRaises(IndexError) as ex:
            i.remove_index(3)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_remove(self):
        i = IntegerList(1,2,3)
        i.remove_index(0)
        self.assertEqual(i.get_data(), [2,3])





if __name__ == '__main__':
    unittest.main()