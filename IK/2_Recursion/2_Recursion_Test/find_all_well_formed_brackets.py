'''
Find All Well Formed Brackets
Problem Statement:
Given a positive integer n, find ALL well formed round brackets string of length 2*n.
The purpose of this problem is to learn recursion and not DP. So, you must write at least one recursive solution. After
that, you can write a DP solution if you want.
Input/Output Format For The Function:
Input Format:
There is only one argument denoting integer n.
Output Format:
Return array of strings res, containing all possible well formed round brackets string. (Length of each string will be
2*n).
You need not to worry about the order of strings in res.
E.g. For n = 2, ["(())", "()()"] or ["()()", "(())"], both will be accepted.

Input/Output Format For The Custom Input:
Input Format:
There should be one line for input, containing an integer n.
If n = 3, then input should be:
3

Output Format:
Let’s denote the size of res is m, where res is the resultant array of string returned by the solution function.
Then, there will be m lines of output, where ith line contains res[i], denoting string at index i of res.

For input n = 3, output will be:
((()))
(()())
(())()
()(())
()()()

Constraints:
1 <= n <= 13
Only use round brackets. '(' and ')'.
Sample Test Case:
Sample Input:
3
Sample Output:
[
   "((()))",
   "(()())",
   "(())()",
   "()(())",
   "()()()"
]

(This is one of the possible outputs. Array containing these five string in any order, will be accepted.)
'''

import sys
import os

# Complete the function below.

def find_all_well_formed_brackets(n):
    pass


if __name__ == "__main__":
    f = sys.stdout

    n = int(input())

    res = find_all_well_formed_brackets(n);
    for res_cur in res:
        f.write( str(res_cur) + "\n" )


    f.close()

'''
There are many possible solutions for this problem.
Have a look at the solution provided by us.
Time Complexity:
O(2n * catalan number(n)).

Auxiliary Space Used:
O(2n * catalan number(n)).
Space Complexity:
O(2n * catalan number(n)).
'''
'''
OPENING_BRACKET = '('
CLOSING_BRACKET = ')'


def find_all_well_formed_brackets(n):
    output = []
    if not n:
        return output
    in_arr = [None] * 2 * n

    def _generate_well_formed_brackets(left_remaining, right_remaining, start):
        # invalid case - number of closing brackets is greater than number of opening brackets
        if left_remaining < 0 or left_remaining > right_remaining:
            return

        if left_remaining == 0 and right_remaining == 0:
            output.append(''.join(in_arr))
            return

        # add opening bracket and recurse
        in_arr[start] = OPENING_BRACKET
        _generate_well_formed_brackets(left_remaining - 1, right_remaining, start + 1)

        # add closing bracket and recurse
        in_arr[start] = CLOSING_BRACKET
        _generate_well_formed_brackets(left_remaining, right_remaining - 1, start + 1)

        # set back arr
        in_arr[start] = None

    _generate_well_formed_brackets(n, n, 0)
    return output



print find_all_well_formed_brackets(1)
print find_all_well_formed_brackets(2)
print find_all_well_formed_brackets(3)

'''
