'''
n Queen Problem

Problem Statement:
The n queen problem is the problem of placing n chess queens on an n * n chessboard, so that no two queens attack each
other.
Your task is to find ALL possible arrangements for the n queen problem.
You have to solve this problem using recursion. (There may be other ways of solving this problem, but for the purpose
of this exercise, please use recursion only).
A queen can move horizontally, vertically, or diagonally.

Input Format:
There is only one argument denoting integer n.

Output Format:
Return 2-D string array of size, number of solutions * n, where length of each string is n.
Any character in string should contain one of 'q' or '-'. Character 'q' means queen is present and character '-' means it is empty.
(To be more clear about the output, look at the sample test case.)

Constraints:
1 <= n <= 13
Sample Test Case:

Sample Input:
4

Sample Output:
Suppose name of the returned array is ret.
ret [0] =
        [

        "--q-",

        "q---",

        "---q",

        "-q--"

        ]

ret [1] =
        [

        "-q--",

        "---q",

        "q---",

        "--q-"

        ]

Explanation:
There are 2 possible solutions for 4 queen problem, hence size of ret is 2 * 4, and length of each string is 4.

ret [i] will denote ith arrangement.
ret [i][j] will denote jth row of ith arrangement.
ret [i][j][k] will denote kth character (if it is a queen or empty cell) of jth row in ith arrangement.

You need not to worry about the order of arrangements in your returned. So output

ret [0] =
        [

        "-q--",

        "---q",

        "q---",

        "--q-"

        ]
        1302

ret [1] =
        [

        "--q-",

        "q---",

        "---q",

        "-q--"

        ]
        2031
will also be considered as a valid answer.

Notes:
For slow languages like Python, test case having n = 13, might not pass, so if your solution passes all other test
cases, then consider your solution as correct solution.
'''

def not_a_threatend_space(queens, row_to_check):
    # [0, 2 , 2, 3]
    for r in range(row_to_check):
        if queens[row_to_check] == queens[r]:
            return False
        if abs(queens[row_to_check]-queens[r])==abs(row_to_check - r):
            return False
    return True

def create_solution(queens):
    solution = []
    for queen in queens:
        line = '-'*len(queens)
        line = line[:queen] + 'q' + line[queen+1:]
        solution.append(line)
    return solution

def n_queens(queens, r, solutions):
    if r == len(queens):
        solutions.append(create_solution(queens))
        return

    for c in range(len(queens)):
        queens[r] = c
        if not_a_threatend_space(queens,r):
            n_queens(queens, r+1, solutions)

def find_all_arrangements(n):
    if n in [0,2,3]:
        return []
    if n == 1:
        return ['q']

    solutions = []
    queens = ['-']*n
    n_queens(queens, 0, solutions)
    return solutions

print(find_all_arrangements(4))
