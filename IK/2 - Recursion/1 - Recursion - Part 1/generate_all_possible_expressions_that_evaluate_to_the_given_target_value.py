'''
Generate All Possible Expressions That Evaluate To The Given Target Value
Problem Statement:
You are given a string s of length n, containing only numerical characters ('0' - '9'). You are also given a
non-negative number target.

You have to put between each pair of numerical characters, one of ("", "*", "+") operators such that the expression you
get will evaluate to the target value.
You have to return ALL possible strings(expressions) that evaluate to target value.

Putting "" (an empty string) operator between two numerical characters means, that the they are joined (e.g. 1""2 = 12).
 Also the join can be extended further (e.g. 1""2""3 = 123).
Precedence of the operators matters. In higher to lower precedence:
Join ("") > Multiplication ("*") > Addition ("+")

The purpose of this problem is to learn recursion and not DP. So, you must write at least one recursive solution. After
that, you can write a DP solution if you want.

Input/Output Format For The Function:
Input Format:
There are two arguments.
1) String s.
2) Long integer target.

Output Format:
Return array of strings res, containing ALL possible strings that evaluate to the target value.
You need not to worry about the order of strings in your output array. Like for s = "22" and target = 4,
arrays ["2+2", "2*2"] and ["2*2", "2+2"] both will be accepted.

Any string in the returned array should not contain any spaces. In the above example string "2+2" is expected, other
strings containing any space like " 2+2", "2 + 2", "2 +2" etc. will give wrong answer.

Input/Output Format For The Custom Input:
Input Format:
The first line of input should contain a string s, denoting input string. The second line should contain an integer
target, denoting the target value as explained in problem statement section.
If s = “222” and target = 24, then input should be:
222
24

Output Format:

Let’s denote the size of res as m, where res is the resultant array of strings returned by solution function.
Then, there will be m lines of output, where ith line contains a string res[i], denoting value at index i of res.

For input s = “222” and target = 24, output will be:
2+22
22+2

Constraints:
1 <= n <= 13
s contains only numerical characters ('0' - '9').
0 <= target < 10^13

Sample Test Cases:
Sample Input:
s = "222"
target = 24

Sample Output:
["22+2", "2+22"]

Explanation:
1) 22 + 2 = 24 (Here, we put "" operator between the first two characters and then put "+" operator between the
last two characters.)
2) 2 + 22 = 24 (Here, we put "+" operator between the first two characters and then put "" operator between the
last two characters.)

Notes:
Suggested time in interview: 40 minutes.
The “Suggested Time” is the time expected to complete this question during a real-life interview, not now in homework
i.e. For the first attempt of a given homework problem, the focus should be to understand what the problem is asking,
what approach you are using, coding it, as well as identifying any gaps that you can discuss during a TC session. Take
your time, but limit yourself to 2 one hour sessions for most problems.
'''

import sys
import os

# Complete the function below.

def generate_all_expressions(s, target):
    pass

if __name__ == "__main__":
    f = sys.stdout

    try:
        s = str(input())
    except:
        s = None

    target = int(input());

    res = generate_all_expressions(s, target);
    for res_cur in res:
        f.write( str(res_cur) + "\n" )


    f.close()

'''
Have a look at the solution provided by us, it contains detailed comments.
Time Complexity:
O((3^(n - 1)) * n).
To solve the problem we just have to use brute force. 
Generate all possible expressions and evaluate them. 
Store the expressions that evaluates to the target.
Now, first let's find how many different expressions possible to generate by putting either of 3 operators in between
each pair of characters.

We have 3 operators to put in n - 1 places (we have n characters in the given string hence n - 1 places between them). 
So simply it is 3^(n - 1). It means for given string of length n, we will have 3^(n - 1) different expressions to check.
What will be the length of expressions?
If we only put "" (join) operator then length of expression will be minimum and that will be n.
Else if we put one of "+" or "*" operators at each of the n - 1 places, then length of the string will be maximum and 
that is 2 * n - 1.
So in general we can write that length of any expression will be O(n). 
So, we have 3^(n - 1) different expressions with O(n) length. So, time complexity will be O((3^(n - 1)) * n).

Auxiliary Space Used:
O((3^(n - 1)) * n).

In worst case all the generated expressions will evaluate to the given target. 
Try:
s = "0000000000000"
target = 0

So in our answer we will store all 3^(n - 1) expressions of length O(n).

Space Complexity:
O((3^(n - 1)) * n).

Auxiliary space used is O((3^(n - 1)) * n) and input size is O(n) hence O((3^(n - 1)) * n) + O(n) -> O((3^(n - 1)) * n).
'''

'''
OPTIMIAL SOLUTION

# ------------------------------------------ START ------------------------------------------

def generate_all_expressions(num, target):
    """
    :type num: str
    :type target: int
    :rtype: List[str]
    """
    if not num:
        return []
    output = []

    def _dfs(so_far, evaluated, idx, prev):
        """
        :param so_far: expression so far (string)
        :param evaluated: evaluated value so far (int)
        :param idx: index to start recursing from
        :param prev: prev value to use for the multiplication special case to give it precedence (explained
            in comments)
        :return: doesn't return, appends to output in the base case
        """
        if idx == len(num):
            if evaluated == target:
                output.append(so_far)
            return

        for i in range(idx, len(num)):
            # For an input like 1234, depending on idx, curr will be 1, 12, 123, 1234; 2 23 234; 3 34; 4 (all
            #   possible splits)
            # This takes care of the concat case as concat has most precedence
            curr = num[idx:i+1]
            curr_int = int(curr)
            if idx == 0:
                # just appending digits for this pass
                # this can be outside the recursive function before dfs is called, but having it here makes
                # it more DRY since we will have to do the curr and curr_int outside otherwise for 1234 case,
                #   when idx = 0, we will have 1, 12, 123, 1234
                # prev value is just current_int (which is same as evaluated)
                _dfs(so_far + curr, curr_int, i+1, curr_int)
            else:
                _dfs(so_far + '+' + curr, evaluated+curr_int, i+1, curr_int)
                # Detailed explanation - 
                #   https://github.com/InterviewKickstart/CodingProblemsIK/blob/master/2 - Recursion/Generate_All_Possible_Expressions_That_Evaluate_To_The_Given_Target_Value/solutions/optimal_solution.cpp
                # In short we need to give precedence to multiplication - eg if we have a + b * c, we really
                #   want a + (b*c) and not (a+b) * c;
                # Having the evaluated so far value say s and prev value passed up b (for addition b, and
                #   for multiplication a * b), will help us evaluate correctly
                # For prev addition; ev = (a + b), prev = b, curr = c; so current calculation
                #   (ev - prev) + (prev * curr) will give us (a + b - b) + (b * c) = a + (b * c)
                # For prev multiplication; ev = (a * b), prev = a * b, curr = c; so current calculation
                #   (ev - prev) + (prev * curr) will give us (a * b - a * b) + (a * b * c) = a * b * c
                # For prev subtraction (in LC) ; ev = (a - b), prev = -b, curr = c; so current calculation
                #   (ev - prev) + (prev * curr) will give us (a - b + b) + (-b * c) = a - (b * c)
                _dfs(so_far + '*' + curr, (evaluated-prev) + (prev*curr_int), i+1, prev*curr_int)

    _dfs('', 0, 0, 0)
    return output

# ------------------------------------------ STOP ------------------------------------------

# MAIN/SAMPLE INPUT


print(generate_all_expressions('1234', 24))

'''
