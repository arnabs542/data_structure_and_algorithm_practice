# Given a 2d array with each cell containing an integer and the ability to move left, right, or down return the maximum
# sum of all numbers in the matrix.
#
# Notes
# You can traverse an cell more than once, but it counts as neutral (0) towards your score after you've used it once
# You are done when you've hit the last row and stops moving
#
# Example (given a 4x5 matrix)
#
# INPUT
# 4 5
# 1 2 3 -1 -2
# -5 -8 -1 2 -150
# 1 2 3 -250 100
# 1 1 1 1 20
#
# Expected Output
# 37
#
# Explanation
# The path we traversed was 1,2,3,-1,2,-1,3,2,1,1,1,1,1,20
# Note that we hit the same -1 twice, but only count it once, making the total 37 not 36.


