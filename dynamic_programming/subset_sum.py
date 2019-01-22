'''
Given an array and a target sum determine if there is a subset of the array that can make the target sum (True/False).
'''

def subset_sum(arr, target):
    rows = len(arr)
    cols = target+1
    grid = [[False]*cols for r in range(rows)]

    for r in range(rows):
        grid[r][0] = True

    for i in range(rows):
        for j in range(cols):
            if i == 0:
                if i == j or j == 0:
                    grid[i][j] = True
                else:
                    grid[i][j] = False
            if j >= arr[i]:
                grid[i][j] = grid[i-1][j-arr[i]] or grid[i-1][j]
            else:
                grid[i][j] = grid[i-1][j]

    return grid[-1][-1]

print(subset_sum([2,3,7,8,10], 11))
print(subset_sum([2,11], 11))
print(subset_sum([11], 11))
print(subset_sum([12], 11))
