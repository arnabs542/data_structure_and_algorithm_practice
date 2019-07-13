import os
import sys

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

if __name__ == "__main__":
    fptr = sys.stdout

    arr1_count = int(input())

    arr1 = []

    for _ in range(arr1_count):
        arr1_item = int(input())
        arr1.append(arr1_item)

    arr2_count = int(input())

    arr2 = []

    for _ in range(arr2_count):
        arr2_item = int(input())
        arr2.append(arr2_item)

    res = merger_first_into_second(arr1, arr2)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

arr1 = [1, 3, 5]
arr2 = [2, 4, 6, 0, 0, 0]
print(merger_first_into_second(arr1, arr2))


'''
=== EDITORIAL ===
We are allowed to use only constant extra space. 

We can start merging from the end. (Or we can first create empty space at the beginning instead of the end by 
copying arr2[i] to arr2[n + i] for i from 0 to n - 1, and then start merging from the beginning. But this will 
add one more loop unnecessarily.)

Have a look at the solution provided by us. 
Time Complexity:
O(n) as we are traversing through the arr1 and arr2 only once.

Auxiliary Space Used:
O(1).

Space Complexity:
O(n) due to input size.

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def merger_first_into_second(A1, A2):
    if not A1 or len(A2) != 2*len(A1):
        return None

    n = len(A1)
    # move elements of second array to the end
    j = 0
    for i in range(n, 2*n):
        swap(arr2, i, j)
        j += 1

    # now we can merge start of A1 with end of A2
    j, k = 0, n
    for i in range(2*n):
        if j == n:
            A2[i] = A2[k]
            k += 1
        elif k == 2*n:
            A2[i] = A1[j]
            j += 1
        elif A1[j] < A2[k]:
            A2[i] = A1[j]
            j += 1
        else:
            A2[i] = A2[k]
            k += 1
    return A2


arr1 = [1, 3, 5]
arr2 = [2, 4, 6, 0, 0, 0]
print merger_first_into_second(arr1, arr2)
'''
