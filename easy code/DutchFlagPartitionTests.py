import unittest
from DutchFlagPartition import dutch_flag_partition

class Test(unittest.TestCase):

    def simple_test(self):
        self.assertEquals([0, 2, 1, 3, 8, 4, 9, 10, 14, 5, 7], dutch_flag_partition(5, [0,2,7,8,3,4,9,10,14,5,1]))
    
    def simple_test1(self):
        self.assertEquals([5,65,43,567,864,1000,1234,56434,5430], dutch_flag_partition(3, [5,43,864,1000,1234,567,56434,65,5430]))

if __name__ == "__main__":
    unittest.main()