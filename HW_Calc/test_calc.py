import unittest

from calc import Calc

class TestCalc(unittest.TestCase):

    def setUp(self):
        pass

    def test_of_test(self):
        self.assertTrue(True)

    def test_add(self):
        result = Calc.add(2, 2)
        self.assertEqual(result, 4)

    def test_sub(self):
        result = Calc.sub(10, 5)
        self.assertEqual(result, 5)

    def test_sub_negative(self):
        result = Calc.sub(5, 10)
        self.assertEqual(result, -5)

    def test_mult(self):
        result = Calc.mult(5, 5)
        self.assertEqual(result, 25)

    def test_division(self):
        result = Calc.division(10, 5)
        self.assertEqual(result, 2)

    def test_division_0(self):
        result = Calc.division(10, 0)
        self.assertEqual(result, None)

    def test_degree(self):
        result = Calc.degree(10, 2)
        self.assertEqual(result, 100)

    def test_remainder(self):
        result = Calc.remainder(100, 50)
        self.assertEqual(result, 0)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()