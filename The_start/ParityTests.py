# imput binary number -> output number of 1s(odd or even)


import unittest
from Parity import parity 


class Test(unittest.TestCase):
    def test_simple_case(self):
        self.assertEquals(0, parity(0b10001000))
    def test_simple_case1(self):
        self.assertEquals(1, parity(int('1011', 2)))

    def test_experimenting_with_booleans(self):
        a = 0b1001
        b = 0b1111
        out = a ^ b
        self.assertEquals(0b0110, out)

if __name__ == "__main__":
    unittest.main()