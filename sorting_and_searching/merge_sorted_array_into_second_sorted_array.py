'''
Merge First Sorted Array Into Second Sorted Array
Problem Statement:
Given two arrays sorted in increasing order:
1) arr1 of size n which contains n positive integers sorted in increasing order.
2) arr2 of size 2n (twice the size of first) which also contains n positive integers sorted in increasing order in its
first half. Second half of this array is empty. (Empty elements are marked by 0).

Write a function that takes these two arrays, and merges the first one into second one, resulting in one fully
increasingly sorted array of 2n positive integers.

Input Format:
There are two arguments. First one is an integer array denoting arr1 of size n and second one is also an integer array
denoting arr2 of size 2n.

Output Format:
Return arr2 containing 2n increasingly sorted positive integers.

Constraints:
1 <= n <= 10^5
1 <= arr1[i] <= 2 * 10^9
1 <= arr2[i] <= 2 * 10^9 (for the first half)
arr2[i] = 0 (for the second half)
You can use only constant extra space.
0 denotes an empty space.

Sample Input:
n = 3
arr1 = [1 3 5]
arr2 = [2 4 6 0 0 0]

Sample Output:
arr2 = [1 2 3 4 5 6]
'''


def merger_first_into_second(arr1, arr2):
    #
    # Write your code here.
    #
    one = len(arr1) - 1
    two = len(arr1) - 1
    i = len(arr2) - 1
    while i >= 0 and one >= 0 and two >= 0:
        if arr1[one] > arr2[two]:
            arr2[i] = arr1[one]
            one -= 1
        else:
            arr2[i] = arr2[two]
            two -= 1
        i -= 1

    while one >= 0:
        arr2[i] = arr1[one]
        one-=1
        i-=1
    while two >= 0:
        arr2[i] = arr2[two]
        two-=1
        i-=1
    return arr2

arr1 = [1, 3, 5]
arr2 = [2, 4, 6, 0, 0, 0]
print(merger_first_into_second(arr1, arr2))
