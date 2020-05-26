# function, which subtracts one list from another and returns the result.


def array_diff(matrix, numforElim):
    res = []
    for num in matrix:
        if num not in numforElim:
            res.append(num)
    return res


import unittest


class Test(unittest.TestCase):
    def test_remove_island(self):
        self.assertEquals([1], array_diff([1, 2, 2], [2]))


if __name__ == "__main__":
    unittest.main()
