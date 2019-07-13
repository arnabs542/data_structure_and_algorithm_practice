import sys
import os

'''
Group the numbers
Problem Statement:
You are given an integer array arr, of size n. Group and rearrange them (in-place) into evens and odds in such a way
that group of all even integers appears on the left side and group of all odd integers appears on the right side.

Input/Output Format For The Function:
Input Format:
There is only one argument: Integer array arr.

Output Format:
Return the same integer array, with evens on left side and odds on the right side.
There is no need to preserve order within odds or within evens.

Input/Output Format For The Custom Input:
Input Format:
The first line of input should contain an integer n, denoting size of input array arr. In next n lines, ith line should
contain an integer arr[i], denoting a value at index i of arr.

If n = 4 and arr = [1, 2, 3, 4], then input should be:
4
1
2
3
4

Output Format:
There will be n lines of output, where ith line contains an integer res[i], denoting value at index i of res.
Here, res is the result array returned by solution function.

For input n = 4 and arr = [1, 2, 3, 4], output will be:
4
2
1
3

Constraints:
1 <= n <= 10^5
arr contains only positive integers.
arr may contains duplicate numbers.
Solution with linear time complexity and constant auxiliary space is expected.

Sample Test Case:
Sample Input:
[1, 2, 3, 4]

Sample Output:
[4, 2, 1, 3]

Explanation:
Order does not matter. Other valid solution are
[2, 4, 1, 3]
[2, 4, 3, 1]
[4, 2, 3, 1]
'''

# Complete the function below.

def solve(arr):
    even_index = 0
    for cur in range(len(arr)):
        if arr[cur]%2 == 0:
            arr[even_index],arr[cur] = arr[cur],arr[even_index]
            even_index += 1
    return arr

if __name__ == "__main__":
    f = sys.stdout

    arr_cnt = 0
    arr_cnt = int(input())
    arr_i = 0
    arr = []
    while arr_i < arr_cnt:
        arr_item = int(input())
        arr.append(arr_item)
        arr_i += 1

    res = solve(arr);
    for res_cur in res:
        f.write( str(res_cur) + "\n" )

    f.close()


'''
=== EDITORIAL ===
We will maintain two pointers, left and right pointer. All the values to the left of left pointer are even and all 
values to the right of right pointer are odd.

We will keep decrementing right and keep incrementing left till the time they do not cross each other. Left pointer
will point to the next pointer which needs to be swapped when we encounter an even number from the right.

Here are two possible scenarios at right pointer
If we encounter an odd number, we simply reduce right.
If we encounter even number, we swap it and move left. We do not move right as the swapped number might be even.
Although we know that number swapped at left is odd, so we move left by one.

Time Complexity: O(n)
We are either incrementing left or decrementing right. Thus, the time complexity is linear, similar to two pointer 
approach.

Space Complexity: O(1) 
We do not use any auxiliary data-structure for storage. We have constant space complexity.


def solve(nums):
    if not nums or len(nums) == 1:
        return nums

    _group_nums(nums, 0, len(nums)-1)
    return nums

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def _group_nums(nums, left, right):
    while left < right:
        while left < len(nums) and nums[left] % 2 == 0:
            left += 1
        while right >= 0 and nums[right] % 2 != 0:
            right -= 1

        if left < right:
            swap(nums, left, right)


n = [1, 2, 3, 4, 5, 6, 1, 3, 5, 8, 9, 10]
solve(n)
print n

n = [1, 1, 3, 3, 5]
solve(n)
print n

n = [1, 2, 3, 4]
solve(n)
print n
'''

