'''
Strings Interleave
Problem Statement:
You're given three strings a, b and i. Write a function that checks whether i is an interleaving of a and b.
String i is said to be interleaving string a and b, if:
len(i) = len(a) + len(b).
i only contains characters present in
 a or b.
i contains all characters of a. From a, any character a[index] should be added exactly once in i.
i contains all
 characters of b. From b, any character b[index] should be added exactly once in i.
Order of all characters in individual
 strings (a and b) is preserved.
Input Format:
You will be given three strings a, b and i.
Strings can contain
Small alphabets - a-z
Large alphabets - A-Z
Numbers - 0-9
Output Format:
Return a boolean if i is an interleaving of a and b.
Constraints:
0 <= len(a), len(b) <= 1000
0 <= len(i) <= 2000
Sample Test Case:
Sample Input-1:
a = "123"
b = "456"
i = "123456"
Sample Output-1:
True
Sample Input-2:
a = "AAB"
b = "AAC"
i = "AAAABC"
Sample Output-2:
True
Sample Input-3:
a = "AAB"
b = "AAC"
i = "AAABAC"
Sample Output-3:
True
'''
import math
import os
import random
import re
import sys


#
# Complete the 'doStringsInterleave' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#  3. STRING i
#
def doStringsInterleave(a, b, i):
    pass




if __name__ == "__main__":
    fptr = sys.stdout
    a = input()
    b = input()
    i = input()
    result = doStringsInterleave(a, b, i)
    fptr.write(str(int(result)) + '\n')
    fptr.close()

'''
Brute force recursive solution:
First character in i should match first character in a or first character in b.
* If it matches first character in a, try matching second character in i with second character in a or first character in b
* If it matches first character in b, try matching second character in i with second character in b or first character in a
* If it matches none of them, terminate with a false

Hence, keep recursing for the rest of the strings. This is an exponential solution, O(2^(len(a)+len(b))) as you can either pick a character from a or a character from b. 


Optimal solution (optimal_solution.cpp):
Convention: str[0 : x] = first x chars of str.
We can say that i[0 : (a_i + b_i)] is an interleaving of a[0 : a_i] and b[0 : b_i], if at least one of the below two is true:
1) 
  - i[0 : (a_i + b_i - 1)] should be an interleaving of a[0 : (a_i - 1)] and b[0 : b_i]
  and
  - a[ai - 1] == i[ai + bi - 1].

or

2) 
  - i[0 : (a_i + b_i - 1)] should be an interleaving of a[0 : a_i] and b[0 : (b_i - 1)]
  and 
  - b[bi - 1] == i[ai + bi - 1].

We can use DP to keep track of the already calculated values. Have a look at the solution for more detials.

Space Complexity: O(len(a) * len(b))
Time Complexity: O(len(a) * len(b))
'''
'''
BRUTE FORCE
# https://leetcode.com/problems/interleaving-string/description/

######## Start ########

#
# Complete the 'doStringsInterleave' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#  3. STRING i
#

def doStringsInterleave(a, b, i):
    # Write your code here
    return string_interleave_rec(a, b, i)

def string_interleave_rec(s1, s2, s3):
    len_s1 = len(s1)
    len_s2 = len(s2)
    len_s3 = len(s3)
    if len_s3 != len_s1 + len_s2:
        return False

    def _string_interleave(i, j):
        # base case
        if i == len_s1 and j == len_s2 and i + j == len_s3:
            return True
        
        if i < len_s1 and j < len_s2 and s1[i] == s2[j] and s2[j] == s3[i+j]:
            # if all 3 are same take from either string
            return _string_interleave(i+1, j) or _string_interleave(i, j+1)
        elif i < len_s1 and s1[i] == s3[i+j]:
            return _string_interleave(i+1, j)
        elif j < len_s2 and s2[j] == s3[i+j]:
            return _string_interleave(i, j+1)
        else:
            return False

    return _string_interleave(0, 0)

######## End ########

str1 = 'abc'
str2 = 'defg'
str3 = 'abdcefg'
print doStringsInterleave(str1, str2, str3)
print '\n'

c = '1234'
a = '123'
b = '123'
print doStringsInterleave(a, b, c)
print '\n'

c = '112233'
a = '123'
b = '123'
print doStringsInterleave(a, b, c)
print '\n'

c = '123456'
a = '123456'
b = ''
print doStringsInterleave(a, b, c)
print '\n'

c = '12345678'
a = '1234'
b = '5678'
print doStringsInterleave(a, b, c)
print '\n'

c = '12345678'
a = '1233'
b = '5678'
print doStringsInterleave(a, b, c)
print '\n'

c = 'XXXXZY'
a = 'XXY'
b = 'XXZ'
print doStringsInterleave(a, b, c)
print '\n'

c = 'XXXXZY'
a = 'XYX'
b = 'XXZ'
print doStringsInterleave(a, b, c)
'''
'''
OPTIMAL SOLUTION
# https://leetcode.com/problems/interleaving-string/description/

######## Start ########

#
# Complete the 'doStringsInterleave' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#  3. STRING i
#

def doStringsInterleave(a, b, i):
    # Write your code here
    return string_interleave_dp(a, b, i)

def string_interleave_dp(s1, s2, s3):
    len_s1 = len(s1)
    len_s2 = len(s2)
    len_s3 = len(s3)
    if len_s3 != len_s1 + len_s2:
        return False
    
    dp = [[False] * (len_s2+1) for _ in range(len_s1+1)]

    # recursion is going from start to end, so dp will go from end to start
    # initial values are i == len_s1 and j == len_s2
    dp[len_s1][len_s2] = True
    # we also need to pre-populate the last row and last column
    # to do that, we need to do a suffix match
    # for row, column is exhausted and we need to match the row and vice versa for column
    # fill last column (match with s1)
    for i in range(len_s1-1, -1, -1):
        # to get corresponding character of s3, do a difference of lengths and add i
        dp[i][len_s2] = dp[i+1][len_s2] and s1[i] == s3[len_s3-len_s1+i]

    # fill last row (match with s2)
    for j in range(len_s2-1, -1, -1):
        # to get corresponding character of s3, do a difference of lengths and add j
        dp[len_s1][j] = dp[len_s1][j+1] and s2[j] == s3[len_s3-len_s2+j]
        
    for i in range(len_s1-1, -1, -1):
        for j in range(len_s2-1, -1, -1):
            if i < len_s1 and j < len_s2 and s1[i] == s2[j] and s2[j] == s3[i + j]:
                dp[i][j] = dp[i+1][j] or dp[i][j+1]
            elif i < len_s1 and s1[i] == s3[i+j]:
                dp[i][j] = dp[i+1][j]
            elif j < len_s2 and s2[j] == s3[i+j]:
                dp[i][j] = dp[i][j+1]

    return dp[0][0]

######## End ########


str1 = 'abc'
str2 = 'defg'
str3 = 'abdcefg'
print doStringsInterleave(str1, str2, str3)
print '\n'

c = '1234'
a = '123'
b = '123'
print doStringsInterleave(a, b, c)
print '\n'

c = '112233'
a = '123'
b = '123'
print doStringsInterleave(a, b, c)
print '\n'

c = '123456'
a = '123456'
b = ''
print doStringsInterleave(a, b, c)
print '\n'

c = '12345678'
a = '1234'
b = '5678'
print doStringsInterleave(a, b, c)
print '\n'

c = '12345678'
a = '1233'
b = '5678'
print doStringsInterleave(a, b, c)
print '\n'

c = 'XXXXZY'
a = 'XXY'
b = 'XXZ'
print doStringsInterleave(a, b, c)
print '\n'

c = 'XXXXZY'
a = 'XYX'
b = 'XXZ'
print doStringsInterleave(a, b, c)
'''
