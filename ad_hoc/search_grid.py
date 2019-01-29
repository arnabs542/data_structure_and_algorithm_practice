def validSpace(r, c, numRows, numColumns, lot):
    if r > numRows-1 or r< 0:
        return False
    if c > numColumns-1 or c< 0:
        return False
    if lot[r][c] == 0:
        return False
    if lot[r][c] == -1:
        return False
    return True

def search(r,c, numRows, numColumns, lot, memo):
    if lot[r][c] == 9:
        return 0
    if (r,c) in memo:
        return memo[(r,c)]
    lot[r][c] = -1
    up = float('inf')
    down = float('inf')
    left = float('inf')
    right = float('inf')

    if validSpace(r-1, c, numRows, numColumns, lot):
        up = search(r-1, c, numRows, numColumns, lot, memo)
    if validSpace(r+1, c, numRows, numColumns, lot):
        down = search(r+1, c, numRows, numColumns, lot, memo)
    if validSpace(r, c-1, numRows, numColumns, lot):
        left = search(r, c-1, numRows, numColumns, lot, memo)
    if validSpace(r, c+1, numRows, numColumns, lot):
        right = search(r, c+1, numRows, numColumns, lot, memo)
    memo[(r,c)] = 1 + min(left, right, up, down)
    return memo[(r,c)]

def top_down_memoization_solution(numRows, numCols, lot):
    memo = dict()
    return search(0, 0, numRows, numCols, lot, memo)

# lot = [
#     [1,0,0],
#     [1,0,0],
#     [1,9,1]
# ]

# lot = [
#     [1,1,1],
#     [0,0,1],
#     [1,9,1]
# ]

lot = [
    [1,1,1,1],
    [0,0,0,1],
    [1,9,1,1]
]
print(top_down_memoization_solution(3, 4, lot))
