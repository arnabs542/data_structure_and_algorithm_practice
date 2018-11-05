# Problem Statement : Given a cost matrix Cost[][] where Cost[i][j] denotes the Cost of visiting cell with
# coordinates (i,j), find a min-cost path to reach a cell (x,y) from cell (0,0) under the condition that you can only
# travel one step right or one step down. (We assume that all costs are positive integers)

matrix = [[1, 2, 3],
          [4, 8, 2],
          [1, 5, 3]]

def minimum_cost_path(matrix, i, j, x, y):
    return minimum_cost_rec(matrix, i, j, x, y)

def minimum_cost_rec(matrix, i, j, x, y):
    if i == x and j == y:
        return matrix[i][j]

    down = right = diagonal = float('inf')

    if i+1>0 and i+1 < x+1:
        down = minimum_cost_rec(matrix, i+1, j, x, y)

    if j+1>0 and j+1 < y+1:
        right = minimum_cost_rec(matrix, i, j+1, x, y)

    if down != float('inf') and right != float('inf'):
        diagonal = minimum_cost_rec(matrix, i+1, j+1,x,y)

    return matrix[i][j] + min(down, right, diagonal)

print(minimum_cost_path(matrix, 0, 0, 2, 2))


