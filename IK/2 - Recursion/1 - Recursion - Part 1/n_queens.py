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
Any character in string should contain one of 'q' or '-'. Character 'q' means queen is present and character '-' means
it is empty.
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
import sys
import os

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

if __name__ == "__main__":
    f = sys.stdout

    n = int(input())

    res = find_all_arrangements(n)
    for i in range(0, len(res)):
        for j in range(0, len(res[i])):
            f.write(res[i][j] + "\n")
        if i != len(res) - 1:
            f.write("\n")


    f.close()


'''
We have provided 3 solutions for the problem (other_solution.cpp, optimal_solution.cpp and optimal_solution2.cpp), 
all of them uses backtracking.
optimal_solution.cpp is an improvement over other_solution.cpp.
Queen can move horizontally, vertically, or diagonally.
No two queens to attack each other, we need to satisfy the following conditions:

1) There must be only one queen in one row.
2) There must be only one queen in one column.
3) There must be only one queen in diagonal from top-left to bottom-right (that is like \ , so we will call it 
back-slash diagonal.)
4) There must be only one queen in diagonal from top-right to bottom-left (that is like / , so we will call it 
slash diagonal.)

We can start placing queens row wise, from top row to bottom row. Once we have placed any queen in any row we will move 
to next next row. (So this will ensure that condition 1 is satisfied!) Now for condition 2, 3 and 4 we can perform a 
check before placing queen at any position.
This was very basic overview. Once look at the other_solution.cpp and it will be more clear.
In other_solution.cpp, is_safe function will visit one slash diagonal, one back-slash diagonal and one column, to check
if there is any clash. So this function is O(n). But it can be easily reduced to O(1). Let's see how.

Lets take n = 5,
so matrix 5 * 5, with positions will look like:
00 01 02 03 04
10 11 12 13 14
20 21 22 23 24
30 31 32 33 34
40 41 42 43 44

1) identify column of element matrix[row][col] as:
0 1 2 3 4
0 1 2 3 4
0 1 2 3 4
0 1 2 3 4
0 1 2 3 4
that is column id = "col".
2) identify slash diagonal of element matrix[row][col] as:
0 1 2 3 4
1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8
that is slash diagonal id = "row + col".
3) identify back-slash diagonal of element matrix[row][col] as:
4 3 2 1 0
5 4 3 2 1
6 5 4 3 2
7 6 5 4 3
8 7 6 5 4
that is back-slash diagonal id = "row - col + n - 1".

Number of columns are n (from 0 to n - 1).
Number of slash and back-slash diagonals are 2*n - 1 (from 0 to 2*n - 2).

Now we can take 3 boolean vectors, one for columns, one for slash diagonals and one for back-slash diagonals.
When we put any queen we can mark appropriate column, slash diagonal and back-slash diagonal as occupied.
Now in is_safe function instead of looping, we only need to check if any of the column, slash diagonal or back-slash 
diagonal is used or not.
Have a look at the optimal_solution.cpp and it will be more clear.

Now let's discuss optimal_solution2.cpp.
We know that in one row we will have only one queen (and total n queens), so instead of 2-D grid we can store the 
information of queens' position in 1D array.
Grid:
--q-
q---
---q
-q--
has queens at positions,
row -> col
0 -> 2,
1 -> 0,
2 -> 3,
3 -> 1

In a 1D array it can be represented as:
arrangement[0] = 2,
arrangement[1] = 0,
arrangement[2] = 3,
arrangement[3] = 1

So we have the same information now stored in 1D array (space O(n)) instead of 2D array (space O(n^2)).
In this problem, we are asked to return actual grids as answer. So, in this solution what we are doing is that first 
generate all arrangements in 1D and then generate 2D arrangements from 1D arrangements. But in optimal_solution.cpp, 
we are directly generating it. So when we are asked to return the actual grids, this solution is not the best. 
optimal_solution.cpp is better.

But think about the similar question where we are asked to return positions of the n queens as answer (not the actual 
grids). Here optimal_solution2.cpp will be better than both other_solution.cpp and optimal_solution.cpp! Because 
other_solution.cpp and optimal_solution.cpp will first generate 2D grids and then convert to positions, but 
optimal_solution2.cpp will directly find positions, avoiding 2d grids (of O(n^2) space)!

For all three solutions:
Time Complexity is exponential. (Exact bound is complex to derive and explain.)
Auxiliary Space Used is also exponential, as we are storing the valid solutions. (Exact bound is complex to derive and 
explain.)
Space Complexity is also exponential, as auxiliary space used is also exponential. (Exact bound is complex to derive 
and explain.)
(If you are looking at other solutions online and wondering why they are faster, then pay attention that they are 
printing only ONE VALID arrangement, not all possible arrangements!)
'''

'''
OPTIMIAL SOLUTION
# Reference - https://github.com/InterviewKickstart/CodingProblemsIK/blob/master/2 - Recursion/n_Queen_Problem/editorial.txt


# ------------------------------------------ START ------------------------------------------
QUEEN = 'q'
NO_QUEEN = '-'


def find_all_arrangements(n):
    output = []

    # n columns for n rows
    col_occupied = [False] * n

    # for n * n board there are 2*n - 1 diagonals (slash and back slash diagonals)
    slash_diag_occupied = [False] * (2*n-1)
    back_slash_diag_occupied = [False] * (2*n-1)

    # by using auxilary space for col occupied and diags occupied and updating then accordingly this function will run in O(1)
    def is_safe(row, col):
        return not (col_occupied[col] or slash_diag_occupied[row+col] or back_slash_diag_occupied[row-col+n-1])

    def _generate_n_queens(curr_arrangement, row):
        if row == n:
            # make deep copy and append to output
            output.append([''.join(x) for x in curr_arrangement])
            return

        for col in range(0, n):
            if is_safe(row, col):
                # mark this col and both diagonals as being occupied
                curr_arrangement[row][col] = QUEEN
                col_occupied[col] = True
                slash_diag_occupied[row+col] = True
                back_slash_diag_occupied[row-col+n-1] = True

                # try to place queen in the next row
                _generate_n_queens(curr_arrangement, row+1)

                # set back as not occupied
                curr_arrangement[row][col] = NO_QUEEN
                col_occupied[col] = False
                slash_diag_occupied[row+col] = False
                back_slash_diag_occupied[row-col+n-1] = False

    # start recursive function with empty current arrangement and 0 row
    curr_board = [[NO_QUEEN] * n for _ in range(n)]
    _generate_n_queens(curr_board, 0)
    return output


# ------------------------------------------ STOP ------------------------------------------


# MAIN FUNCTION/SAMPLE INPUT


for i in range(0, 6):
    out = find_all_arrangements(i)
    print('for n = ', i)
    print('\n')
    for a in out:
        print('\n'.join(a))
        print('\n')

'''
'''
OPTIMIAL SOLUTION 2
# Reference - https://github.com/InterviewKickstart/CodingProblemsIK/blob/master/2 - Recursion/n_Queen_Problem/editorial.txt


# ------------------------------------------ START ------------------------------------------

def find_all_arrangements(n):
    output = []

    # n columns for n rows
    col_occupied = [False] * n

    # for n * n board there are 2*n - 1 diagonals (slash and back slash diagonals)
    slash_diag_occupied = [False] * (2*n-1)
    back_slash_diag_occupied = [False] * (2*n-1)

    # by using auxilary space for col occupied and diags occupied and updating then accordingly this function will run in O(1)
    def is_safe(row, col):
        return not (col_occupied[col] or slash_diag_occupied[row+col] or back_slash_diag_occupied[row-col+n-1])

    def _generate_n_queens(curr_arrangement, row):
        if row == n:
            output.append([x for x in curr_arrangement])
            return

        for col in range(0, n):
            if is_safe(row, col):
                # mark this col and both diagonals as being occupied
                curr_arrangement[row] = col
                col_occupied[col] = True
                slash_diag_occupied[row+col] = True
                back_slash_diag_occupied[row-col+n-1] = True

                # try to place queen in the next row
                _generate_n_queens(curr_arrangement, row+1)

                # set back as not occupied
                col_occupied[col] = False
                slash_diag_occupied[row+col] = False
                back_slash_diag_occupied[row-col+n-1] = False

    # start recursive function with empty current arrangement and 0 row
    _generate_n_queens([None]*n, 0)
    return generate_output(output)


def generate_output(boards):
    output = []
    for arr in boards:
        o = [['-'] * len(arr) for _ in range(len(arr))]
        for r, c in enumerate(arr):
            o[r][c] = 'q'
        # join rows
        output.append([''.join(row) for row in o])
    return output


# ------------------------------------------ STOP ------------------------------------------


# MAIN FUNCTION/SAMPLE INPUT


# for i in range(0, 6):
#     out = find_all_arrangements(i)
#     print('for n = ', i)
#     print('\n')
#     for a in out:
#         print('\n'.join(a))
#         print('\n')
out = find_all_arrangements(5)
print(out)
print(len(out))
'''
