import unittest
from calculator import *

class testCalc(unittest.TestCase):

    def test_add(self):
        result = add(2, 1)
        self.assertEqual(result, 3)

    def test_sub(self):
        result = sub(10, 1)
        self.assertEqual(result, 9)

    def test_mul(self):
        result = add(3, 3)
        self.assertEqual(result, 9)

    def test_div(self):
        result = add(10, 2)
        self.assertEqual(result, 5)

if __name__=="__main__":
    unittest.main()