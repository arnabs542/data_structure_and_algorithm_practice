from collections import deque
'''
Shortest distance between two cells in a matrix or grid
Given a matrix of N*M order. Find the shortest distance from a source cell to a destination cell, traversing through
limited cells only. Also you can move only up, down, left and right. If found output the distance else -1.

s represents ‘source’
d represents ‘destination’
* represents cell you can travel
0 represents cell you can not travel
This problem is meant for single source and destination.

Examples:

Input : {'0', '*', '0', 's'},
        {'*', '0', '*', '*'},
        {'0', '*', '*', '*'},
        {'d', '*', '*', '*'}
Output : 6

Input :  {'0', '*', '0', 's'},
         {'*', '0', '*', '*'},
         {'0', '*', '*', '*'},
         {'d', '0', '0', '0'}
Output :  -1

'''

def is_valid(grid, i, j):
    if i >= len(grid):
        return False
    if j >= len(grid[0]):
        return False
    if grid[i][j] == '0':
        return False
    return True

def shortest_path_to_dest_cell(grid, source_cell):
    q = deque()
    visited = set()
    distance = dict()
    q.appendleft(source_cell)
    directions = [(-1,0), (1,0), (0,1), (0,-1)]
    while len(q) > 0:
        row,col = q.pop()
        grid[row][col] = visited.add((row,col))
        for d in directions:
            if is_valid(grid, row+d[0], col+d[1]):
                q.appendleft((row+d[0],col+d[1]))

    return -1
