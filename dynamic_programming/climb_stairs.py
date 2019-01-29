'''
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in [0, 1, 2]:
            return n

        prev = 2
        prev_prev = 1
        for i in range(3, n + 1):
            answer = prev_prev + prev
            prev_prev = prev
            prev = answer
        return answer

test = Solution()
print(test.climbStairs(0))
print(test.climbStairs(1))
print(test.climbStairs(2))
print(test.climbStairs(3))
print(test.climbStairs(5))
print(test.climbStairs(25))
print(test.climbStairs(50))
print(test.climbStairs(500))
print(test.climbStairs(5000))
