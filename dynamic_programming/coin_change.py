'''
Given a target sum to reach A and K coins, find the minimum number of coins it would take to reach target A.
'''

def make_change(coins, target):
    rows = len(coins)
    cols = target+1

    grid = [[float('inf')]*cols for r in range(rows)]

    for r in range(rows):
        grid[r][0] = 0

    for i in range(rows):
        for j in range(cols):
            if j >= coins[i]:
                grid[i][j] = min(1+grid[i][j-coins[i]], grid[i-1][j])
            else:
                grid[i][j] = grid[i-1][j]

    return grid[rows-1][cols-1]

print(make_change([1,5,6,8], 11))
