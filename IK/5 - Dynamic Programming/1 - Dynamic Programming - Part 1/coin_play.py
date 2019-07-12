'''
Coin Play
Problem Statement:
Consider a row of n coins of values v1, . . ., vn. We play a game against an opponent by alternating turns. In each turn,
 a player selects either the first or last coin from the row, removes it from the row permanently, and receives the value
 of the coin. Determine the maximum possible amount of money we can definitely win if we move first.
Assume full competency by both players.
Input/Output Format For The Function:
Input Format:
You will be given an array of integers v.
Output Format:
Return an integer max, denoting the maximum possible amount of sum that you can accumulate.
Input/Output Format For The Custom Input:
Input Format:
The first line should contain an integer n, denoting no. of coins. In next n lines, ith line should contain an integer vi,
 denoting value of ith coin in input array v.
If n = 4 and v = [8, 15, 3, 7], then input should be:
4
8
15
3
7
Output Format:
There will be only one line, containing an integer max, denoting the maximum possible amount of sum that you can accumulate.

For input n = 4 and v = [8, 15, 3, 7], output will be:
22
Constraints:
1 <= n <= 1000
1 <= v[i] <= 10^6
Sample Test Case:
Sample Input:
v = [8, 15, 3, 7]
Sample Output:
22
Explanation:
Player 1 can start two different ways: either picking 8 or picking 7. Depending on the choice s/he makes, the end reward
 will be different. We want to find the maximum reward the first player can collect.
1. Player 1 start by picking coin of amount 8.
Remaining v = [15, 3, 7].
Opponent will have two choices, either pick coin of value 15 or 7. Opponent will always pick 15 (to maximize his/her own
 amount).
Remaining v = [3, 7].
Player 1 will have two choices, either pick coin of value 3 or 7.
Player 1 will always pick 7 (to maximize his/her own amount).
Hence in this case, player 1 can get maximum amount 8 + 7 = 15.
(This is greedy strategy i.e. pick the highest at every step.)
2. Player 1 start by picking coin of amount 7.
Remaining v = [8, 15, 3].
Opponent will have two choices, either pick coin of value 8 or 3.
Opponent will pick 8 (to maximize his/her own amount). (Even if he/she picks 3, then also answer will be same, because in
 next turn player 1 is looking for coin of value 15.)
Remaining v = [15, 3].
Player 1 will have two choices, either pick coin of value 15 or 3.
Player 1 will always pick 15 (to maximize his/her own amount).
Hence in this case, player 1 can get maximum amount 7 + 15 = 22.
Given these two strategies, we want 22 as the answer, and not 15.
'''
import math
import os
import random
import re
import sys

# Complete the maxWin function below.
def maxWin(v):
    pass



if __name__ == "__main__":
    fptr = sys.stdout
    v_count = int(input())
    v = []
    for _ in range(v_count):
        v_item = int(input())
        v.append(v_item)
    res = maxWin(v)
    fptr.write(str(res) + '\n')
    fptr.close()


'''
Recursive solution
There are two choices:
1. The user chooses the ith coin with value Vi: The opponent either chooses (i+1)th coin or jth coin. The opponent intends
 to choose the coin which leaves the user with minimum value.
i.e. The user can collect the value Vi + min(F(i+2, j), F(i+1, j-1) )
coinGame1
2. The user chooses the jth coin with value Vj: The opponent either chooses ith coin or (j-1)th coin. The opponent intends
 to choose the coin which leaves the user with minimum value.
i.e. The user can collect the value Vj + min(F(i+1, j-1), F(i, j-2) )
Recurrence relationship
F(i, j) ==> represents the maximum value the user can collect from i'th coin to j'th coin.
F(i, j) = Max(Vi + min(F(i+2, j), F(i+1, j-1)), Vj + min(F(i+1, j-1), F(i, j-2) )) 
Base Cases
F(i, j) = Vi      If j == i
F(i, j) = max(Vi, Vj) If j == i+1
Optimal solution
We can memoize the recurrence relationship mentioned above or build an iterative version for the same problem.
Space Complexity: O(n^2)
Time Complexity: O(n^2)
'''
'''
# Recursive solution
def max_win(coins):
    def _max_win_rec(i, j):
        if i == j:
            return coins[i]
        if j == i+1:
            return max(coins[i], coins[j])
        if i > j:
            return float('inf')

        # option 1
        # player 1 picks coin[i] and player 2 will try to maximize from coin i + 1 and j, so will have to min of i + 2 and j - 1
        # option 2
        # player 1 picks coin[j] and player 2 will try to maximize from coin i and j-1, so will have to min of i + 1 and j - 2
        return max(coins[i] + min(_max_win_rec(i+2, j), _max_win_rec(i+1, j-1)), coins[j] + min(_max_win_rec(i+1, j-1), _max_win_rec(i, j-2)))

    return _max_win_rec(0, len(coins)-1)


# DP solution
def coins_max_profit_dp(coins):
    n = len(coins)

    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = coins[i]

    # for any case where i > j we have inf, so we can ignore that (anything below the diagonal
    # the diagonal is i == j which from recursion we know is equal to the coins array
    # in recursion i goes from 0 -> end and j goes from end -> 0; so reverse that in dp
    # i goes from end -> 0 and j goes from 0 -> end (we make it go only from we only want from diagonal going forward
    # apply some boundary conditions to check for i, j bounds
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if i == j:
                dp[i][j] = coins[i]
                continue

            o1 = dp[i+2][j] if i < n-2 else float('inf')
            o2 = dp[i+1][j-1] if i < n - 1 and j > 0 else float('inf')
            o3 = dp[i][j-2] if j > 1 else float('inf')

            dp[i][j] = max(coins[i] + min(o1, o2), coins[j] + min(o2, o3))

    return dp[0][n-1]


c = [8, 15, 3, 7]
print max_win(c)
print coins_max_profit_dp(c)
'''
