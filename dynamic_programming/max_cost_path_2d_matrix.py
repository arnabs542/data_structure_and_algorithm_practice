from datetime import datetime, timedelta
import unittest

'''
Find the max cost to get from cell 0,0 to cell n,m in an nxm matrix. Valid directions include moving down and right.
'''

def bottom_up(grid):
    rows = len(grid)
    cols = len(grid[0])
    tabulation = [[0]*(cols+1) for _ in range(rows+1)]

    for row in range(rows-1, -1, -1):
        for col in range(cols-1, -1, -1):
            tabulation[row][col] = grid[row][col] + max(tabulation[row+1][col], tabulation[row][col+1])

    return tabulation[0][0]

class MaximumCostTest(unittest.TestCase):

    def test_one(self):
        grid = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]

        self.assertEqual(bottom_up(grid), 29)
        print("Passed")

    def test_two(self):
        grid = [
            [4,3],
            [2,1],
        ]

        self.assertEqual(bottom_up(grid), 8)
        print("Passed")

    def test_three(self):
        grid = [
            [19,5],
            [7,120],
        ]

        self.assertEqual(bottom_up(grid), 146)
        print("Passed")

    def test_four(self):
        grid = [
            [19]
        ]

        self.assertEqual(bottom_up(grid), 19)
        print("Passed")

    def test_maximum_cost_path_times(self):
        grid = [[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20],
                   [21, 22, 23, 24, 25]]
        start_time = datetime.now()
        self.assertEqual(bottom_up(grid), 149)
        print("Maximum cost path bottom up = " + str(datetime.now() - start_time))

test = MaximumCostTest()
test.test_one()
test.test_two()
test.test_three()
test.test_four()
test.test_maximum_cost_path_times()
