'''
Count ways to reach the N’th stair
Problem Statement:
(This is simple. Make me proud.)
There are n stairs, a person standing at the bottom wants to reach the top. He can climb a certain number of steps at once.
 For instance, the person can climb either 1 stair or 2 stairs at a time. Count the number of ways, the person can reach
 the top.
Note: Solve the problem for general case i.e. for n stairs, and different kinds of steps that can be taken (e.g. instead
 of only 1 or 2 steps, it could be 2, 3 and 5 steps at a time).
Input/Output Format For The Function:
Input Format:
There will be two arguments: steps and n.
An array of integer steps denotes the steps the person can climb at a time and an integer n denotes the total number of
 stairs to be climbed.
Note: Answer is guaranteed to fit in long integer.
Output Format:
Return an integer ways, denoting the number of ways to reach the last staircase.
Input/Output Format For The Custom Input:
Input Format:
The first line should contain m(let say), denoting size of steps array. In next m lines, ith line should contain steps[i],
 denoting ith value in array steps. In the next line, there should be an integer, denoting n.
If n = 7 and steps = [2, 3], then input should be:
2
2
3
7
Output Format:
There will be one line, containing an integer ways, denoting the number of ways to reach the last staircase.
For input n = 7 and steps = [2, 3], output will be:
3
Constraints:
1 <= n <= 100
1 <= steps <= 10000
All values in steps will be unique. There are no duplicate entries.
Sample Test Cases:
Sample Test Case 1:
Sample Input 1:
n = 1
steps = [1, 2]
Sample Output 1:
1
Explanation 1:
Only one way to reach = [{1}]
Sample Test Case 2:
Sample Input 2:
n = 2
steps = [1, 2]
Sample Output 2:
2
Explanation 2:
Two ways to reach = [{1, 1}, {2}]
Sample Test Case 3:
Sample Input 3:
n = 7
steps = [2, 3]
Sample Output 3:
3
Explanation 3:
Three ways to reach = [{2, 2, 3}, {2, 3, 2}, {3, 2, 2}]
'''
import math
import os
import random
import re
import sys

# Complete the countWaysToClimb function below.
def countWaysToClimb(steps, n):
    pass



if __name__ == "__main__":
    fptr = sys.stdout
    steps_count = int(input())
    steps = []
    for _ in range(steps_count):
        steps_item = int(input())
        steps.append(steps_item)
    n = int(input())
    res = countWaysToClimb(steps, n)
    fptr.write(str(res) + '\n')
    fptr.close()

'''
Let us try to solve this problem for 1, 2 and 3 stairs.
Recursive solution
We will denote s(n) as the number of ways to reach nth stair using given stairs, which would be 1, 2 and 3 in our explanation.

We can reach n from n-1, n-2 and n-3 by adding 1 stair of 1, 2 and 3 respectively.
Thus we get the following relationship
s(n) = s(n-1) + s(n-2) + s(n-3)
Base case would be 0. We can reach 0 by only starting there. Thus, s(0) = 1
Optimal solution
We can memoize the recurrence relationship mentioned above or build an iterative version for the same problem.
We can see for any random stair x, s(x) depends on s(y), where y < x. Thus we can iteratively move from 0 to n and at each
 step we can have
s[x] = s[x-1] + s[x-2] + s[x-3]
and s[n] will be the final answer.
Space Complexity: O(n*length(steps))
Time Complexity: O(n*(length(steps))
'''
'''
import java.util.TreeSet;

public class OptimalSolution {
    /*
     * Space Complexity: O(n*length(steps))
     * Time Complexity: O(n*(length(steps))
     */
    private static long countWaysToClimb(int[] steps, int n) {
        /*
         * We will store counts till every step.
         */
        long countTillHere[] = new long[n + 1];
        // There is one way to reach till zero, as we start from 0
        countTillHere[0] = 1;
        for (int i = 1; i <= n; i++) {
            // Find the ways that you can reach here from current step
            for (int step : steps) {
                int previousStep = i - step;
                if (previousStep >= 0) {
                    countTillHere[i] += countTillHere[previousStep];
                }
            }
        }
        
        // Ways to reach the nth step
        return countTillHere[n];
    }
}
'''
