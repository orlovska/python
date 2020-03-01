import unittest
from BuyAndSell import buy_and_sell_stock_once

class Test(unittest.TestCase):

    def first_test(self):
        input1 = [310,315,275,295,260,270,290,230,255,250]
        self.assertEquals(30, buy_and_sell_stock_once(input1))

    def second_test(self):
        input2 = [310,436,567,300,312,600]
        self.assertEquals(300, buy_and_sell_stock_once(input2))

    def no_profit_test(self):
        input1 = [260,270,290,300,400]
        self.assertEquals(0, buy_and_sell_stock_once(input1))

if __name__ == "__main__":
    unittest.main()