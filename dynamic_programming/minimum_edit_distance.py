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

