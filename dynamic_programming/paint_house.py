'''
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of
painting each house with a certain color is different. You have to paint all the houses such that no two adjacent
houses have the same color.
The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0]
is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so
on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:
Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
     Minimum cost: 2 + 5 + 3 = 10.
'''

def top_down_rec(costs, cur_house, last_color, memo):
    if cur_house == len(costs):
        return 0

    if (cur_house,last_color) in memo:
        return memo[(cur_house,last_color)]

    min_cost = float('inf')
    for color_index in range(len(costs[cur_house])):
        if color_index == last_color:
            min_cost = min(min_cost, float('inf'))
        else:
            min_cost = min(min_cost, costs[cur_house][color_index] + top_down_rec(costs, cur_house+1, color_index, memo))

    memo[(cur_house,last_color)] = min_cost
    return memo[(cur_house,last_color)]

def top_down(costs):
    memo = dict()
    return top_down_rec(costs, 0, -1, memo)

# def bottom_up(costs):
#     dp = dict()
#     for cur_house in range(len(costs)):
#         for color_index in range(len(costs[cur_house])):
#             if color_index == last_color:
#                 min_cost = min(min_cost, float('inf'))
#             else:
#                 min_cost = min(min_cost, costs[cur_house][color_index] + top_down_rec(costs, cur_house+1, color_index))
#         return min_cost
#

costs = [[17,2,17],[16,16,5],[14,3,19]]
print(top_down(costs))
