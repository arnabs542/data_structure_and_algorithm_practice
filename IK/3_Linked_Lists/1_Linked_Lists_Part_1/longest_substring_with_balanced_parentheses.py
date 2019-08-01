'''
Longest Substring With Balanced Parentheses
Problem Statement:
Given a string brackets, containing only '(' and ')', you have to find the length of the longest substring that has balanced
 parentheses.
You need to find length only, not the substring itself.
Input/Output Format For The Function:
Input Format:
There is only one argument in input brackets, denoting input string.
Output Format:
Return an integer res, denoting the length of the longest  substring that has balanced parentheses.
Input/Output Format For The Custom Input:
Input Format:
There should be only one line of input, containing a string brackets, denoting input string of parentheses.
If brackets = “((((())(((()”, then input should be:
((((())(((()
Output Format:
There will be one line, containing an integer res, denoting the result returned by the solution function.
For input brackets = “((((())(((()”, output will be:
4
Constraints:
    * 1 <= | brackets | <= 10^5
    * Input string only contains '(' and ')' characters.
Sample Test cases:
Sample Test Case 1:
Sample Input 1:
"((((())(((()"
Sample Output 1:
4
Explanation 1:
"(())"
Sample Test Case 2:
Sample Input 2:
"()()()"
Sample Output 2:
6
Explanation 2:
"()()()"
'''
import sys
import os

# Complete the function below.

def find_max_length_of_matching_parentheses(brackets):
    pass


if __name__ == "__main__":
    f = sys.stdout

    try:
        brackets = str(input())
    except:
        brackets = None

    res = find_max_length_of_matching_parentheses(brackets);
    f.write(str(res) + "\n")


    f.close()


'''
A brute force solution is to find all substrings and check if they have matching parentheses. This will be a solution with
 O(n*n*n) time complexity, (n*(n-1)/2) substrings with O(n) check for matching.
Now observation to make is that, if a matching '(' isn't found for any ')', then string till ')' can no longer be part of
 the substring we are looking for. i.e. "(()))()()" now at 4th position no maching '(' is found for ')', hence part "(()))"
 is not needed in further calculations!
So if we end with a non-matching closing parenthesis i, we can just jump to the string starting after i. 
Now have a look at the code provided by us.
Time Complexity:
O(n).
Auxiliary Space Used:
O(n).
As we are using stack to store the indices of the opening brackets.
Space Complexity:
O(n).
As input is O(n) and auxiliary space used is also O(n). So, O(n) + O(n) -> O(n).
'''
'''
STARTING_PAREN = '('


def find_max_length_of_matching_parentheses(brackets):
    if len(brackets) == 0:
        return 0

    stack = []
    start, prev_start, max_len = 0, 0, 0

    for i, bracket in enumerate(brackets):
        if bracket == STARTING_PAREN:
            stack.append(i)
        else:
            # bracket is closing
            if not stack:
                # stack is empty, found a closing paren but no open paren, advance to next char
                prev_start = i + 1
            else:
                # matching paren found, compute the length of the matching paren
                # if stack is empty - compute length from previous position, otherwise length of
                # matching substring is however far i has gotten from top of stack
                stack.pop()
                start = prev_start - 1 if not stack else stack[-1]
                size = i - start
                max_len = max(size, max_len)

    return max_len


string = '(()()())'
# string = '()'

print find_max_length_of_matching_parentheses(string)

"""
Key lessons
- push the index of the paren on the stack so we can find out the prev start and also keep track of max size
- push if a start paren, else pop and check if it's part of a correct group
"""
'''
