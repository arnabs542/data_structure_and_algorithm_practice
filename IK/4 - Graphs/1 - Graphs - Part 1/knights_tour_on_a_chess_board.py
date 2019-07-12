'''
Knight's Tour On A Chess Board
Problem Statement:
You are given a rows * cols chessboard and a knight that moves like in normal chess.
Currently knight is at starting position denoted by start_row th row and start_col th col, and want to reach at ending position
 denoted by end_row th row and end_col th col.
The goal is to calculate the minimum number of moves that the knight needs to take to get from starting position to ending
 position.
start_row, start_col, end_row and end_col are 0-indexed.
Input Format:
There are six arguments. First is an integer denoting rows, second is an integer denoting cols, third is an integer denoting
 start_row, fourth is an integer denoting start_col, fifth is an integer denoting end_row and sixth is an integer denoting
 end_col.
Output Format:
Return an integer.
If it is possible to reach from starting position to ending position then return minimum number of moves that the knight
 needs to take to get from starting position to ending position.
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

import os
import sys

# Complete the function below

from collections import deque


def is_valid(rows, cols, r, c):
    if (0 <= r < rows) and (0 <= c < cols):
        return True
    else:
        return False


def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    pass


if __name__ == "__main__":
    f = sys.stdout

    rows = int(input())

    cols = int(input())

    start_row = int(input())

    start_col = int(input())

    end_row = int(input())

    end_col = int(input())

    res = find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col)

    f.write(str(res) + "\n")

    f.close()



# MY PREVIOUS SOLUTION
# def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
#     # Write your code here.
#     if not is_valid(rows, cols, start_row, start_col) or not is_valid(rows, cols, end_row, end_col):
#         return -1
#     q = deque()
#     directions = [(-1, 2), (1, 2), (-2, 1), (2, 1), (-2, -1), (2, -1), (-1, -2), (1, -2)]
#     visited = set((start_row, start_col))
#     starting_dist = 0
#     q.appendleft((start_row, start_col, starting_dist))
#     while len(q) > 0:
#         row, col, dist = q.pop()
#         if (row, col) == (end_row, end_col):
#             return dist
#         for r, c in directions:
#             if is_valid(rows, cols, row + r, col + c) and (row + r, col + c) not in visited:
#                 visited.add((row + r, col + c))
#                 q.appendleft((row + r, col + c, dist + 1))
#     return -1
'''
This is a simple BFS problem.

Have a look at the solution provided by us, it contains necessary comments to understand the solution.

Time Complexity:
O(rows * cols).

Auxiliary Space Used:
O(rows * cols).

Space Complexity:
O(rows * cols). 
Input is O(1) and auxiliary space used is O(rows * cols). So, O(1) + O(rows * cols) -> O(rows * cols).
'''
'''
from collections import deque

DIRECTIONS = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]


def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    def get_neighbors(r, c):
        neighbors = []
        for dr, dc in DIRECTIONS:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < rows and 0 <= new_c < cols:
                neighbors.append((new_r, new_c))

        return neighbors

    start_cell = start_row, start_col

    # visited set to keep track of visited cells
    visited = {start_cell}

    # make a queue with cell and number of moves to get to that cell
    q = deque([(start_cell, 0)])

    while q:
        cell, count = q.popleft()
        if cell == (end_row, end_col):
            return count

        # using * operator to convert tuple into 2 arguments as get_neighbors function expects
        for new_cell in get_neighbors(*cell):
            if new_cell not in visited:
                q.append((new_cell, count + 1))
                visited.add(new_cell)

    return -1


print find_minimum_number_of_moves(5, 5, 0, 0, 4, 1)
'''
