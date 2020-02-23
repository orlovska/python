# input: two digits -> output X in power of Y
# 0, 1 -> 0
# 1, 1 -> 1
# 2, 2 - > 4

import unittest
from XinPowerY import power 


class Test(unittest.TestCase):
    def test_simple_case(self):
        self.assertEquals(0, power(0, 1))
    def test_simple_case1(self):
        self.assertEquals(1, power(1, 2))

    def test_negative_number(self):
        self.assertEquals(0.11111111, power(3, -2))

if __name__ == "__main__":
    unittest.main()