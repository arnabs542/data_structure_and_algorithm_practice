'''
Edit Distance
'''

# def edit_distance(word1, word2):
#     rows = len(word2)+1
#     cols = len(word1)+1
#     grid = [[0]*cols for _ in range(rows)]
#
#     for i in range(1, rows):
#         grid[i][0] = i
#     for j in range(1, cols):
#         grid[0][j] = j
#
#     for i in range(rows):
#         for j in range(cols):
#             if word2[i] == word1[j]:
#                 grid[i][j] =
#
#     for i in range(rows):
#         for j in range(cols):
#             print(grid[i][j], end=" ")
#         print()
#
# edit_distance('abcdef', 'azced')


def edit_distance_rec(word1, word2, i, j):
    if i == len(word1):
        return len(word2)-j
    if j == len(word2):
        return len(word1)-i

    if word1[i] == word2[j]:
        return edit_distance_rec(word1, word2, i+1, j+1)

    return 1+min(edit_distance_rec(word1, word2, i+1, j),
               edit_distance_rec(word1, word2, i, j+1),
               edit_distance_rec(word1, word2, i+1, j+1))

def edit_distance(word1, word2):
    return edit_distance_rec(word1, word2, 0, 0)

# print(edit_distance("ball", "sballz"))


# def edit_distance_bottom_up(word1, word2):
#     dp = [[0]*(len(word2)+1) for i in range(len(word1)+1)]
#
#     for i in range(len(word1)+1):
#         dp[i][0] = i
#
#     for j in range(len(word2)+1):
#         dp[0][j] = j
#
#     for i in range(len(word1)-1, -1, -1):
#         for j in range(len(word2)-1, -1, -1):
#             if word1[i] == word2[j]:
#                 dp[i][j] = dp[i+1][j+1]
#             else:
#                 dp[i][j] = 1 + min(dp[i+1][j],
#                                    dp[i+1][j+1],
#                                    dp[i][j+1])
#     return dp[0][0]
#
# print(edit_distance_bottom_up("ball", "sballz"))


'''
'''
