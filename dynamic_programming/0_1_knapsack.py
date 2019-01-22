'''
Given a list of items with their weights and their values, what is the max amount of loot you can get considering the
max bag capacity is X?

'''

def zero_one_knapsack(weight_value_pairs, bag_capacity):
    rows = len(weight_value_pairs)
    cols = bag_capacity+1
    grid = [[0]*cols for r in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if j >= weight_value_pairs[i][0]:
                grid[i][j] = max(weight_value_pairs[i][1] + grid[i-1][j-weight_value_pairs[i][0]], grid[i-1][j])
            else:
                grid[i][j] = grid[i-1][j]

    for i in range(rows):
        for j in range(cols):
            print(grid[i][j], end=" ")
        print()

    return grid[-1][-1]

print(zero_one_knapsack([(1,1), (3,4), (4,5), (5,7)], 7))
