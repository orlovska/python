# input: list of numbers --> output: True or False 
# [0, 1] - > False
# [0] - > True
# [1, 0] - > True 
# [3, 0, 2, 3, 0, 0, 1] - > True
# [3,3,1,0,2,0,1] - > True
# [3,2,0,0,2,0,1] - > False 


import unittest
from AdvancingThroughAnArray import can_reach_end

class Test(unittest.TestCase):

    def test_from_book(self):
        self.assertEquals(True, can_reach_end([3,3,1,0,2,0,1]))

    def test_one_element(self):
        self.assertEquals(True, can_reach_end([0]))
    
    def test_two_true(self):
        self.assertEquals(True, can_reach_end([1, 0]))

    def test_two_false(self):
        self.assertEquals(False, can_reach_end([0, 1]))
    
    def test_5(self):
        self.assertEquals(True, can_reach_end([3, 0, 2, 3, 0, 0, 1]))

    def test_6(self):
        self.assertEquals(False, can_reach_end([3,2,0,0,2,0,1]))

if __name__ == "__main__":
    unittest.main()