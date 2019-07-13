'''
Possible To Achieve Target Sum?
Problem Statement:
Given an integer array arr of size n and a target sum k, you have to determine, whether there exists a non-empty
group of numbers (numbers need not to be contiguous) in arr such that their sum equals to k.
The purpose of this problem is to learn recursion and not DP. So, you must write at least one recursive solution.
After that, you can write a DP solution if you want.

Input/Output Format For The Function:
Input Format:
There are two argument. First one is arr and second one is k.
Output Format:
Return a boolean flag, denoting your answer.

Input/Output Format For The Custom Input:
Input Format:
The first line of input should contain an integer n, denoting size of input array arr. In next n lines, ith line
should contain an integer arr[i], denoting value at index i of arr. In the next line, there should be an integer k,
denoting the target sum value.
If n = 3, arr = [2, 4, 8] and k = 6, then input should be:
3
2
4
8
6

Output Format:
There will be one line of output, containing “0” or “1” (without quotes), corresponding to the result returned by
solution function. “0” denotes flag = False and “1” denotes flag = True.
For input n = 3, arr = [2, 4, 8] and k = 6, output will be:
1

Constraints:
1 <= n <= 18
-10^17 <= arr[i], k <= 10^17

Sample Test Cases:
Sample Test Case 1:
Sample Input 1:
arr = [2 4 8]
k = 6

Sample Output 1:
True

Explanation 1:
arr[0] + arr[1] = 6
Sample Test Case 2:
Sample Input 2:
arr = [2 4 6]
k = 5

Sample Output 2:
False
Explanation 2:
There does not exists any group such that its sum equals to k.

Notes:
Maximum time allowed in interview: 20 Minutes.
'''

import sys
import os


def check_if_sum_possible(arr, k):
    pass

if __name__ == "__main__":
    f = sys.stdout

    arr_cnt = 0
    arr_cnt = int(input())
    arr_i = 0
    arr = []
    while arr_i < arr_cnt:
        arr_item = int(input());
        arr.append(arr_item)
        arr_i += 1


    k = int(input());

    res = check_if_sum_possible(arr, k);
    f.write(str(int(res)) + "\n")


    f.close()


'''
If you are passing all the testcases except 2, then you are missing one special case. Case when k = 0 and none of the 
arr numbers are 0. In this case answer should be false! This is a very common mistake we have seen in most of the 
solutions. ""Even most of the solutions you will find in popular websites will fail"" this testcase!  
Now let's think about the actual solution.
Observe that arr size is too small. (1 <= n <= 18). So brute force solution is expected.
Try to generate all the possible groups (subsets) and see if sum of elements in current group (subset) equals to k. 
(Of course do not forget to remove empty subset! Otherwise above mentioned testcases will fail!)
When we try to generate all the possible subsets when:
n = 1
total number of subsets = 2
n = 2
total number of subsets = 4
n = 3
total number of subsets = 8
n = 4
total number of subsets = 16
...
Now it is easy to observe that number of different subsets we can get from n numbers is 2^n. 
Now manually try to write down all the possible subsets for n = 3.
Now use bit mask to represent each subset. If we have taken second and third element and not taken first element then 
bitmask should be 011.
Write down all the bitmasks and ""sort them""!
They will look like:
000
001
010
011
100
101
110
111

This pattern can be helpful to solve the problem!
Lets take n = 4: 
0000 
0001 
0010
0011
0100
0101
0110
0111
1000
1001
1010
1011
1100
1101
1110
1111

Look at the first 8 and second 8 masks differently.
First 8 are:
0000 
0001 
0010
0011
0100
0101
0110
0111

From first 8 remove the left most bit 0,
000
001
010
011
100
101
110
111

Ohh! This is the same pattern we got from n = 3!

Second 8 are:
1000
1001
1010
1011
1100
1101
1110
1111

From second part remove the left most bit 1,
000
001
010
011
100
101
110
111

Ohh! This is the same pattern we got from n = 3!

So it means we will not include 1st element and then generate all possible subsets for smaller size (3). Then we will 
include 1st element and then generate all possible subsets for smaller size (3). 

Now have a look at the solution provided by us. It uses the same idea mentioned above. 

Time Complexity:
O(2^n) as we are generating and processing all the possible groups (subsets). 

Next few lines will confuse you but try to understand it. It will surely help you to get better idea about finding time
complexity of algorithms. 
We are generating 2^n subsets,

For n = 3, 
000
001
010
011
100
101
110
111

Consider above as table of 2^n rows and n cols. 
O(2^n) is the cost of iterating over rows in above table, now question may arise what about the cost of iterating 
over cols? Should not the time complexity be O(n * 2^n)? 

Answer is NO. To get the answer better to read some articles on "Amortized Analysis of a Binary Counter". In this 
problem same idea applies and bound is O(2^n) tighter than O(n * 2^n)! 

Auxiliary Space Used:
O(n) due to function call stack (recursion depth).

Space complexity:
O(n) due to input and auxiliary space used.

Also other solution using dp is possible. Very similar to 0-1 knapsack problem having time complexity O(n * k). But 
value stored in arr[i] and k is very large. So this is not the expected solution for the given constraints. Brute 
force solution will perform much much better than this dp solution!
Let's change the constraints:
-100 <= arr[i], k <= 10
1 <= n <= 10^5

Now solution similar to 0-1 knapsack will perform much much better than the brute force solution!

See how changing constraints changes the choice of the algorithm!
'''

'''
# ------------------------------------------ START ------------------------------------------


def check_if_sum_possible(arr, k):

    # generate all subsets and check if any of them sum to the target
    def _check_sum_possible(so_far, idx):
        # base condition
        if idx == len(arr):
            # so_far check makes sure that so_far is not an empty array (requirement of question)
            if so_far and sum(so_far) == k:
                return True
            return False

        # take element and recurse, don't take element and recurse
        return _check_sum_possible(so_far + [arr[idx]], idx+1) or _check_sum_possible(so_far, idx+1)

    return _check_sum_possible([], 0)

# ------------------------------------------ STOP ------------------------------------------


# SAMPLE RUNS/TESTS
A = [2, 4, 8]
check_k = 6
print(check_if_sum_possible(A, check_k))

B = [2, 4, 8]
check_k = 5
print(check_if_sum_possible(B, check_k))

C = [1, 1]
check_k = 0
print(check_if_sum_possible(C, check_k))

D = [2, 10, 20]
check_k = 0
print(check_if_sum_possible(D, check_k))
'''
