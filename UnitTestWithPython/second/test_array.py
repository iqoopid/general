import unittest
from code.arrays import MoreMeth

class TestMoreMeth(unittest.TestCase):

    def setUp(own):
        own.arraymeth = MoreMeth()

    def test_concat(self):
        array2 = ["eta", "theta", "iota", "kappa", "lambda", "mu"]
        a, b = self.arraymeth.concat(array2)
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()