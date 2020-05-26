#input: digit number int type --> ouput: reverse version of it 
# 123 -> 321
# 12 -> 21
# -31 -> -13

import unittest
from ReverseDigits import reverse 


class Test(unittest.TestCase):
    def test_simple_case(self):
        self.assertEquals(321, reverse(123))
    def test_simple_case1(self):
        self.assertEquals(21, reverse(12))

    def test_negative_number(self):
        self.assertEquals(-13, reverse(-31))

if __name__ == "__main__":
    unittest.main()