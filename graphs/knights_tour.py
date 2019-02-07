import unittest
'''

Knight's Tour On A Chess Board
Problem Statement:
You are given a rows * cols chessboard and a knight that moves like in normal chess.
Currently knight is at starting position denoted by start_row th row and start_col th col, and want to reach at
ending position denoted by end_row th row and end_col th col.
The goal is to calculate the minimum number of moves that the knight needs to take to get from starting position
to ending position.

start_row, start_col, end_row and end_col are 0-indexed.

Input Format:
There are six arguments. First is an integer denoting rows, second is an integer denoting cols, third is an integer
denoting start_row, fourth is an integer denoting start_col, fifth is an integer denoting end_row and sixth is an
integer denoting end_col.
Output Format:
Return an integer.

If it is possible to reach from starting position to ending position then return minimum number of moves that the
knight needs to take to get from starting position to ending position.

If it is not possible to reach from starting position to ending position then return -1.

Constraints:
1 <= rows * cols <= 10^5
0 <= start_row, end_row < rows
0 <= start_col, end_col < cols

Sample Test Case:
Sample Input:
rows = 5
cols = 5
start_row = 0
start_col = 0
end_row = 4
end_col = 1

Sample Output:
3

Explanation:
3 moves to reach from (0, 0) to (4, 1):

(0, 0) -> (1, 2) -> (3, 3) -> (4, 1).
'''

from collections import deque

def is_valid(rows, cols, r, c):
    if (0 <= r < rows) and (0 <= c < cols):
        return True
    else:
        return False

def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    # Write your code here.
    if not is_valid(rows,cols,start_row,start_col) or not is_valid(rows,cols,end_row,end_col):
        return -1
    q = deque()
    directions = [(-1,2), (1,2), (-2,1), (2,1), (-2,-1), (2,-1), (-1,-2), (1,-2)]
    visited = set((start_row, start_col))
    starting_dist = 0
    q.appendleft((start_row, start_col, starting_dist))
    while len(q) > 0:
        row,col,dist = q.pop()
        if (row,col) == (end_row,end_col):
            return dist
        for r,c in directions:
            if is_valid(rows,cols,row+r,col+c) and (row+r,col+c) not in visited:
                visited.add((row+r, col+c))
                q.appendleft((row+r, col+c, dist+1))
    return -1

class test_Knight(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(find_minimum_number_of_moves(5,5,0,0,4,1), 3)
        print("Passed")

    def test_one(self):
        self.assertEqual(find_minimum_number_of_moves(5,5,1,1,4,4), 2)
        print("Passed")

    def test_two(self):
        self.assertEqual(find_minimum_number_of_moves(1,1,0,0,0,0), 0)
        print("Passed")

    def test_three(self):
        self.assertEqual(find_minimum_number_of_moves(2,1,1,0,0,0), -1)
        print("Passed")

    def test_four(self):
        self.assertEqual(find_minimum_number_of_moves(2,1,1,0,1,0), 0)
        print("Passed")

    def test_five(self):
        self.assertEqual(find_minimum_number_of_moves(2,2,1,1,0,0), -1)
        print("Passed")

    def test_six(self):
        self.assertEqual(find_minimum_number_of_moves(2,2,1,1,0,1), -1)
        print("Passed")

    def test_seven(self):
        self.assertEqual(find_minimum_number_of_moves(2,2,1,1,1,0), -1)
        print("Passed")

    def test_eight(self):
        self.assertEqual(find_minimum_number_of_moves(2,2,1,1,1,1), 0)
        print("Passed")

    def test_nine(self):
        self.assertEqual(find_minimum_number_of_moves(2,7,0,5,0,1), 2)
        print("Passed")

    def test_ten(self):
        self.assertEqual(find_minimum_number_of_moves(2,7,0,5,1,1), -1)
        print("Passed")

    def test_eleven(self):
        self.assertEqual(find_minimum_number_of_moves(3,8,0,6,1,5), 2)
        print("Passed")

    def test_twelve(self):
        self.assertEqual(find_minimum_number_of_moves(3,8,0,6,1,3), 2)
        print("Passed")

    def test_thirteen(self):
        self.assertEqual(find_minimum_number_of_moves(3,8,0,6,2,0), 4)
        print("Passed")

    def test_fourteen(self):
        self.assertEqual(find_minimum_number_of_moves(1,100000,0,50,0,99999), -1)
        print("Passed")

    def test_fifteen(self):
        self.assertEqual(find_minimum_number_of_moves(99999,1,99991,0,23,0), -1)
        print("Passed")

    def test_sixteen(self):
        self.assertEqual(find_minimum_number_of_moves(2,50000,1,997,0,49997), -1)
        print("Passed")

    def test_seventeen(self):
        self.assertEqual(find_minimum_number_of_moves(49999,2,49993,1,53,0), -1)
        print("Passed")

    def test_eighteen(self):
        self.assertEqual(find_minimum_number_of_moves(33333,3,333,0,33332,2), 16501)
        print("Passed")

    def test_nineteen(self):
        self.assertEqual(find_minimum_number_of_moves(3,33332,1,1599,1,0), 801)
        print("Passed")

    def test_twenty(self):
        self.assertEqual(find_minimum_number_of_moves(4,24975,3,21841,1,13), 10914)
        print("Passed")

    def test_twenty_one(self):
        self.assertEqual(find_minimum_number_of_moves(24982,4,512,0,20480,3), 9985)
        print("Passed")

    def test_twenty_two(self):
        self.assertEqual(find_minimum_number_of_moves(10000,10,9876,8,1234,2), 4322)
        print("Passed")

    def test_twenty_three(self):
        self.assertEqual(find_minimum_number_of_moves(10,9999,0,0,9,9988), 4995)
        print("Passed")

    def test_twenty_four(self):
        self.assertEqual(find_minimum_number_of_moves(20,5000,0,4325,0,3), 2162)
        print("Passed")

    def test_twenty_five(self):
        self.assertEqual(find_minimum_number_of_moves(4999,20,4998,0,4998,19), 11)
        print("Passed")

    def test_twenty_six(self):
        self.assertEqual(find_minimum_number_of_moves(316,316,21,26,313,310), 192)
        print("Passed")

    def test_twenty_seven(self):
        self.assertEqual(find_minimum_number_of_moves(315,316,222,123,123,222), 66)
        print("Passed")

    def test_twenty_eight(self):
        self.assertEqual(find_minimum_number_of_moves(316,315,150,158,173,178), 15)
        print("Passed")

    def test_twenty_nine(self):
        self.assertEqual(find_minimum_number_of_moves(315,315,0,314,314,0), 210)
        print("Passed")

tests = test_Knight()
print("TESTS")
tests.test_one()
tests.test_two()
tests.test_three()
tests.test_four()
tests.test_five()
tests.test_six()
tests.test_seven()
tests.test_eight()
tests.test_nine()
tests.test_ten()
tests.test_eleven()
tests.test_twelve()
tests.test_thirteen()
tests.test_fourteen()
tests.test_fifteen()
tests.test_sixteen()
tests.test_seventeen()
tests.test_eighteen()
tests.test_nineteen()
tests.test_twenty()
tests.test_twenty_one()
tests.test_twenty_two()
tests.test_twenty_three()
tests.test_twenty_four()
tests.test_twenty_five()
tests.test_twenty_six()
tests.test_twenty_seven()
tests.test_twenty_eight()
tests.test_twenty_nine()
print("FINISHED")
