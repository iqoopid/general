import unittest
from my_calculations import Calculations

class TestCalculations(unittest.TestCase):
    # setUp() method runs before each test method, therefore Calculations is initialized each time before the tests.
    def setUp(own):
        own.calculation = Calculations(8, 2)

    def test_sum(self):
        self.assertEqual(self.calculation.get_sum(), 10, 'The sum is wrong.')

    def test_diff(self):
        self.assertEqual(self.calculation.get_difference(), 6, 'The difference is wrong.')

    def test_product(self):
        self.assertEqual(self.calculation.get_product(), 16, 'The product is wrong.')

    def test_quotient(self):
        self.assertEqual(self.calculation.get_quotient(), 4, 'The quotient is wrong.')

    def test_remainder(self):
        self.assertEqual(self.calculation.get_remainder(), 0, 'The remainder is wrong.')


if __name__ == '__main__':
    unittest.main()