import unittest
from Divide import divide


class Test(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(3, divide(9, 3))

    def test_simple_case_1(self):
        self.assertEqual(4, divide(12, 3))

    def test_long_number(self):
        self.assertEqual(9, divide(3279213, 364357))
if __name__ == "__main__":
    unittest.main()
    