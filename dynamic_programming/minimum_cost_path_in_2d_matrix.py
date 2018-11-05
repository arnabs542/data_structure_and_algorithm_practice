from datetime import datetime, timedelta
import unittest

# Problem Statement : Given a cost matrix Cost[][] where Cost[i][j] denotes the Cost of visiting cell with
# coordinates (i,j), find a min-cost path to reach a cell (x,y) from cell (0,0) under the condition that you can only
# travel one step right or one step down. (We assume that all costs are positive integers)

matrix = [[1, 2, 3],
          [4, 8, 2],
          [1, 5, 3]]

def minimum_cost_path_brute_force(matrix, i, j, x, y):
    if i == x and j == y:
        return matrix[i][j]

    down = right = diagonal = float('inf')

    if i+1>0 and i+1 < x+1:
        down = minimum_cost_path_brute_force(matrix, i+1, j, x, y)

    if j+1>0 and j+1 < y+1:
        right = minimum_cost_path_brute_force(matrix, i, j+1, x, y)

    if down != float('inf') and right != float('inf'):
        diagonal = minimum_cost_path_brute_force(matrix, i+1, j+1,x,y)

    return matrix[i][j] + min(down, right, diagonal)


def minimum_cost_path_top_down(matrix, i, j, x, y, memo = None):
    if memo == None:
        memo = dict()

    if i == x and j == y:
        return matrix[i][j]

    key = (i,j)
    if key in memo:
        return memo[key]

    down = right = diagonal = float('inf')

    if i+1>0 and i+1 < x+1:
        down = minimum_cost_path_top_down(matrix, i+1, j, x, y, memo)

    if j+1>0 and j+1 < y+1:
        right = minimum_cost_path_top_down(matrix, i, j+1, x, y, memo)

    if down != float('inf') and right != float('inf'):
        diagonal = minimum_cost_path_top_down(matrix, i+1, j+1,x,y, memo)

    memo[key] = matrix[i][j] + min(down, right, diagonal)
    return memo[key]

class MinimumCostTest(unittest.TestCase):

    def test_one(self):
        matrix1 = [[1, 2, 3],
                   [4, 8, 2],
                   [1, 5, 3]]
        self.assertEqual(minimum_cost_path_brute_force(matrix1, 0, 0, 2, 2), 8)
        self.assertEqual(minimum_cost_path_top_down(matrix1, 0, 0, 2, 2), 8)
        print("Passed ")

    def test_two(self):
        matrix1 = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]
        self.assertEqual(minimum_cost_path_brute_force(matrix1, 0, 0, 2, 2), 15)
        self.assertEqual(minimum_cost_path_top_down(matrix1, 0, 0, 2, 2), 15)
        print("Passed")

    def test_three(self):
        matrix1 = [[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20],
                   [21, 22, 23, 24, 25]]
        self.assertEqual(minimum_cost_path_brute_force(matrix1, 0, 0, 4, 4), 65)
        self.assertEqual(minimum_cost_path_top_down(matrix1, 0, 0, 4, 4), 65)
        print("Passed")

    def test_minimum_cost_path_times(self):
        matrix1 = [[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20],
                   [21, 22, 23, 24, 25]]
        start_time = datetime.now()
        minimum_cost_path_brute_force(matrix1, 0, 0, 4, 4)
        print("Brute force minimum cost path = " + str(datetime.now() - start_time))

        start_time = datetime.now()
        minimum_cost_path_top_down(matrix1, 0, 0, 4, 4)
        print("Minimum cost path top down = " + str(datetime.now() - start_time))


test_minimum_cost = MinimumCostTest()
test_minimum_cost.test_one()
test_minimum_cost.test_two()
test_minimum_cost.test_three()
test_minimum_cost.test_minimum_cost_path_times()
