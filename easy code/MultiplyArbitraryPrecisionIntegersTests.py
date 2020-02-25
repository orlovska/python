import unittest
from MultiplyArbitraryPrecisionIntegers import multiply

class Test(unittest.TestCase):
    def test_simple_case(self):
        self.assertEquals([7, 2], multiply([8], [9]))

    def test_negative(self):
        self.assertEquals([-1, 4, 7, 5, 7, 3, 9, 5, 2, 5, 8, 9, 6, 7, 6, 4, 1, 2, 9, 2, 7], multiply([1,9,3,7,0,7,7,2,1], [-7,6,1,8,3,8,2,5,7,2,8,7]))

if __name__ == "__main__":
    unittest.main()