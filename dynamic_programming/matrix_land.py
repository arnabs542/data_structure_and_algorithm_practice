# Given a 2d array with each cell containing an integer and the ability to move left, right, or down return the maximum
# sum of all numbers in the matrix.
#
# Notes
# You can traverse an cell more than once, but it counts as neutral (0) towards your score after you've used it once
# You are done when you've hit the last row and stops moving
#
# Example (given a 4x5 matrix)
#
# INPUT
# 4 5
# 1 2 3 -1 -2
# -5 -8 -1 2 -150
# 1 2 3 -250 100
# 1 1 1 1 20
#
# Expected Output
# 37
#
# Explanation
# The path we traversed was 1,2,3,-1,2,-1,3,2,1,1,1,1,1,20
# Note that we hit the same -1 twice, but only count it once, making the total 37 not 36.

import math
import os
import random
import re
import sys

# Complete the matrixLand function below.
def matrixLand(A, memo=None):
    '''
    am I a valid position in the matrix?
    have I been to this cell before?
    no
        add cell num to my score
        change cell num to 0 either in matrix or somehow in my own hashmap
        can I explore left, right, or down(are they valid moves?)?
            do I already have a max value for them in the hashmap?
            yes
                return your score
            no
                take the path that gives the highest score
        yes
    yes
    '''
    matrixLand_rec(A, 0, 0, 0)

def matrixLand_rec(A, score, i, j, memo=None):
    if memo == None:
        memo = dict()

    if i >= len(A) or i < 0 or j >= len(A[0]) or j < 0:
        return score

    if (i,j) in memo:
        return 0

    score += A[i][j]
    memo[(i,j)] = A[i][j]

    # change cell num to 0 either in matrix or somehow in my own hashmap
    left = matrixLand_rec(A, score, i, j-1, memo)
    right = matrixLand_rec(A, score, i, j+1, memo)
    down = matrixLand_rec(A, score, i+1, j, memo)
    return max(left, right, down)

if __name__ == '__main__':
    # A = [[1, 2, 3, -1, -2],[-5, -8, -1, 2, -150],[1, 2, 3, -250, 100],[1, 1, 1, 1, 20]]
    # A = [[3, -1, -2],[-1, 2, -150],[3, -250, 100]]
    A = [[3, -2],[3, 100]]


    result = matrixLand(A)

    print(str(result) + '\n')

