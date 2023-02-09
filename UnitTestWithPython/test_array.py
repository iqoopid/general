import unittest
from code.arrays import MoreMeth

class TestMoreMeth(unittest.TestCase):

    def setUp(own):
        array1 = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta"]
        own.arraymeth = MoreMeth(array1)

    def test_concat(self):
        array0 = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa", "lambda", "mu"]
        array2 = ["eta", "theta", "iota", "kappa", "lambda", "mu"]
        a = self.arraymeth.concat(array2)
        self.assertEqual(a, array0)

if __name__ == '__main__':
    unittest.main()