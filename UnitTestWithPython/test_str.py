import unittest
from code.stringMethods import StringMethods

class TestStringMethods(unittest.TestCase):

    def setUp(own):
        own.stringmeth = StringMethods()

    def test_upper(self):
        self.assertEqual(self.stringmeth.if_upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue(self.stringmeth.check_isupper()[0])
        self.assertFalse(self.stringmeth.check_isupper()[1])

    def test_split(self):
        self.assertEqual(self.stringmeth.check_split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            self.stringmeth.check_split(2)

if __name__ == '__main__':
    unittest.main()