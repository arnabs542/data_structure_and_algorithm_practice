#!/bin/python3

'''
You are given a binary matrix as an input. You want to return the number of islands in the binary matrix.
You can think of the 0's as the ocean and the 1's as land.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.


Examples:
# There are 6 islands in this matrix
{1, 1, 0, 0, 0},
{0, 1, 0, 0, 1},
{1, 0, 0, 1, 1},
{0, 0, 0, 0, 0},
{1, 0, 1, 0, 1}

# There is 1 island in this matrix
{1, 1, 1, 1, 1},
{1, 1, 1, 1, 1},
{1, 1, 1, 1, 1}

Followup question: Can you write a function to you return the largest island (island with the most number of 1's)?
'''

import os
import sys


# Complete the function below.

def countIslands(mat):
    rows = len(mat)
    cols = len(mat[0])
    count = 0
    for row in range(rows):
        for col in range(cols):
            if mat[row][col] == 1:
                getIslandFloodfill(row, col, mat)
                count += 1
    return count


def getIslandFloodfill(row, col, mat):
    if mat[row][col] == 1:
        mat[row][col] = 'x'
        if row+1 < len(mat):
            getIslandFloodfill(row+1, col, mat)
        if row-1 > 0:
            getIslandFloodfill(row-1, col, mat)
        if col+1 < len(mat[0]):
            getIslandFloodfill(row, col+1, mat)
        if col-1 > 0:
            getIslandFloodfill(row, col-1, mat)


def largestIsland(mat):
    rows = len(mat)
    cols = len(mat[0])
    largest_island_size = 0
    for row in range(rows):
        for col in range(cols):
            if mat[row][col] == 1:
                current_island_size = getIslandSize(row, col, mat)
                if largest_island_size < current_island_size:
                    largest_island_size = current_island_size
    return largest_island_size


def getIslandSize(row, col, mat):
    if mat[row][col] == 1:
        mat[row][col] = 'x'
        count = 1
        if row+1 < len(mat):
            count += getIslandSize(row+1, col, mat)
        if row-1 > 0:
            count += getIslandSize(row-1, col, mat)
        if col+1 < len(mat[0]):
            count += getIslandSize(row, col+1, mat)
        if col-1 > 0:
            count += getIslandSize(row, col-1, mat)
        return count
    else:
        return 0

# Example 1
# {1, 1, 0, 0, 0},
# {0, 1, 0, 0, 1},
# {1, 0, 0, 1, 1},
# {0, 0, 0, 0, 0},
# {1, 0, 1, 0, 1}
inp = [[1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [1, 0, 0, 1, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 1]]
# inp = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
# print(countIslands(inp))
print(largestIsland(inp))
