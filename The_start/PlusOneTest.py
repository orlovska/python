# Input list -> otput list 
# [1,2,3] -> [1,2,4]
# [1] -> [2]
# [0] -> [1]
# [9] -> [1,0]
# [9,9] -> [1,0,0]
# [1,3,4,6,7,8,5,6,7,8,8,8,8,9] -> [1,3,4,6,7,8,5,6,7,8,8,8,9,0]
# [9] * 12 -> [1] + [0]*12

import unittest
from PlusOne import Solution 
s = Solution()
class Test(unittest.TestCase):
    def test_simple_case(self):
        self.assertEquals([2], s.plusOne([1]))

    def test_simple_case1(self):
        self.assertEquals([1,2,4], s.plusOne([1,2,3]))

    def test_case_zero(self):
        self.assertEquals([1], s.plusOne([0]))
    
    def test_nine(self):
        self.assertEquals([1,0], s.plusOne([9]))

    def test_two_nines(self):
        self.assertEquals([1,0,0], s.plusOne([9,9]))

    def test_long_case(self):
        self.assertEquals([1,3,4,6,7,8,5,6,7,8,8,8,9,0], s.plusOne([1,3,4,6,7,8,5,6,7,8,8,8,8,9]))

    def test_with_multizero(self):
        self.assertEquals([1] + [0]*12, s.plusOne([9] * 12))

if __name__ == "__main__":
    unittest.main()