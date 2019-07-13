'''
Generate All Subsets Of A Set
Problem Statement:
Given a set (in form of string s containing only distinct lowercase letters ('a' - 'z')), you have to generate ALL
possible subsets of it .

Note that:
empty set is always a subset of any set.
whole set s should also be considered as its subset here.

The purpose of this problem is to learn recursion and not DP. So, you must write at least one recursive solution.
After that, you can write a DP solution if you want.
Input/Output Format For The Function:
Input Format:
There is only one argument denoting string s.
Output Format:
Return array of strings res, containing ALL possible subsets of given string.

You need not to worry about order of strings in your output array. E.g. s = "a", arrays ["", "a"] and ["a", ""]  both
will be accepted.
Order of characters in any subset must be same as in the input string. For s = "xy", array ["", "x", "y", "xy"] will
be accepted, but ["", "x", "y", "yx"] will not be accepted.
Input/Output Format For The Custom Input:
Input Format:
The first and only line of input should contain a string s, denoting the input string.
If s = “xy”, then input should be:
xy

Output Format:
Let’s denote the size of res as m, where res is the resultant array of strings returned by the solution function.
Then, there will be m lines of output, where ith line contains string at index i of res.

For input s = “xy”, output will be:

----------- START of output -----------

x
y
xy
----------- END of output ---------------
(Note that the first line of output is an empty line, corresponding to empty set [“”].)

Constraints:
0 <= |s| <= 20
s only contains distinct lowercase alphabetical letters ('a' - 'z').

Sample Test Cases:
Sample Input:
"xy"

Sample Output:
["", "x", "y", "xy"]

Notes:
Suggested time in interview: 20 minutes
The “Suggested Time” is the time expected to complete this question during a real-life interview, not now in homework
i.e. For the first attempt of a given homework problem, the focus should be to understand what the problem is asking,
what approach you are using, coding it, as well as identifying any gaps that you can discuss during a TC session. Take
your time, but limit yourself to 2 one hour sessions for most problems.
'''
import sys
import os

# Complete the function below.
from copy import deepcopy

def generate_all_subsets(string):
    subsets = set()
    get_subsets([], list(string), 0, subsets)
    return list(subsets)


def get_subsets(soFar, rest, r_i, subsets):
    if r_i == len(rest):
        subsets.add(''.join(soFar))
        return
    next = deepcopy(soFar)
    remaining = deepcopy(rest)
    i = r_i
    while i < len(remaining):
        next.append(remaining[i])
        del remaining[i]
        get_subsets(next, remaining, i, subsets)
        next = deepcopy(soFar)
        get_subsets(next, remaining, i, subsets)

if __name__ == "__main__":
    f = sys.stdout

    try:
        s = str(input())
    except:
        s = ""

    res = generate_all_subsets(s);
    for res_cur in res:
        f.write( str(res_cur) + "\n" )


    f.close()

'''
We have provided 2 solutions:
1) Recursive Solution : other_solution.cpp.
2) Iterative Solution : optimal_solution.cpp.

Have a look at both the solutions. 
Both solutions are valid, but recursive solution is slightly slower because of function calls and variable passing.

Also you should observe that number of subsets will always be power of 2.
If size of set is n, then number of subsets will always be 2^n.

Time Complexity:
O(2^n * n).

As we will generate 2^n strings of length O(n).
Auxiliary Space Used:

O(2^n * n).

As we will store 2^n strings of length O(n) in output array to be returned.

Space Complexity:
O(2^n * n).

As auxiliary space used is O(2^n * n) and input is O(n) hence O(2^n * n) + O(n) -> O(2^n * n).
'''

'''
# ------------------------------------------ START ------------------------------------------
def generate_all_subsets(s):
    output = []

    # recursive function to generate subsets
    def _generate_all_subsets(so_far, idx):
        # base case
        if idx == len(s):
            # IK OJ is expecting a list of strings and not a list of lists
            output.append(''.join(so_far))
            return

        # recurse after adding current and not adding current to so_far
        _generate_all_subsets(so_far + [s[idx]], idx+1)
        _generate_all_subsets(so_far, idx+1)

    _generate_all_subsets([], 0)

    return output
# ------------------------------------------ STOP ------------------------------------------

# SAMPLE TEST CASES
a = ['x', 'y', 'z']
print generate_all_subsets(a)
a = ['x']
print generate_all_subsets(a)
a = []
print generate_all_subsets(a)
'''
