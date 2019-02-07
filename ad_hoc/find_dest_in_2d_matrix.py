from collections import deque
'''

'''
def is_valid(grid, r,c):
    if r <= len(grid):
        return True
    if c <= len(grid[0]):
        return True

def bfs(grid, r,c):
    dp = [[(False,float('inf'))]*(len(grid[0])) for _ in range(len(grid))]
    q = deque()
    q.appendleft((r,c))
    directions = [(-1,0), (0,-1), (1,0), (0,1)]
    while len(q) > 0:
        r,c = q.popleft()

        for d in directions:
            if is_valid(grid, r, c):
                q.appendleft(r+d[0], c+d[1])
