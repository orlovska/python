import unittest
from Multiply import multiply


class Test(unittest.TestCase):

    def test_simple_case(self):
        self.assertEquals(8, multiply(2, 4))
    
    def test_simple_case0(self):
        self.assertEquals(45, multiply(5, 9))
        
    def test_simple_case1(self):
        self.assertEquals(0, multiply(0, 2))
