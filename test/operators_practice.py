import unittest

class OperatorsTest(unittest.TestCase):
    def test_equal(self):
        self.assertTrue(5 == 5)

    def test_equal_operator(self):
        a = 7
        b = -2
        self.assertFalse(a == b)

    def test_notequal_operator(self):
        a = 7
        b = 7
        self.assertFalse(a != b)

    def test_greater_than_operator(self):
        a = 7
        b = 5
        self.assertFalse(a < b)

    def test_less_than_operator(self):
        a = 5
        b = 7
        self.assertFalse(a > b)

    def test_less_or_equal_operator(self):
        a = 7
        b = 5
        self.assertFalse(a <= b)

    def test_greater_or_equal_operator(self):
        a = 5
        b = 7
        self.assertFalse(a >= b)


if __name__ == '__main__':
    unittest.main()
