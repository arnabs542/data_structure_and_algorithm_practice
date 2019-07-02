import os
import sys

'''
3 Sum
Problem Statement:
Given an array of N integers, find all triplets that sum to 0 (zero).

Triplets may or may not be consecutive numbers.
The array can include duplicate elements.
Array is not necessarily sorted.
Print output as shown. i.e. as strings, one per line, comma separated elements. See sample for clarity.
Order of elements inside the answer triplets does not matter. i.e. if your output elements are the same, but only in
different order, then it's an acceptable solution.
Do not print duplicate triplets. Eg: 1,1,-2 and 1,-2,1 are duplicates.
If no such triplets are found, then print nothing.

Input Format:
Integer array
Input may or may not be sorted
Repeats possible

Output Format:

Return a String array containing all possible triplets who sum to 0. One String for one triplet.

Order of output does not matter.

Constraints:
1 <= N <= 2000
-10^3 <= element <= 10^3

Given array may contains duplicate numbers.

Sample Test Cases:

Sample Input-1:
arr = [10, 3, -4, 1, -6, 9];

Sample Output-1:
10,-4,-6
3,-4,1

Sample Input-2:
arr = [12, 34, -46];

Sample Output-2:
12,-46,34

Sample Input-3:
arr = [0, 0, 0];

Sample Output-3:
0,0,0

Sample Input-4:
arr = [-2, 2, 0 -2, 2];

Sample Output-4:
2,-2,0
'''
# Brute Force
# def findZeroSum(arr):
#     zeros = set()
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             for k in range(j+1, len(arr)):
#                 if arr[i]+arr[j]+arr[k]==0:
#                     zeros.add(tuple(sorted((arr[i],arr[j],arr[k]))))
#     for triplet in zeros:
#         print('{},{},{}'.format(triplet[0],triplet[1],triplet[2]))

# def findZeroSum(arr):
#     hash = dict()
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if -(arr[i]+arr[j]) in hash:
#                 print('{},{},{}'.format(arr[i],arr[j],-(arr[i]+arr[j])))
#             else:
#                 hash[arr[j]] = j
#
#
# findZeroSum([10, 3, -4, 1, -6, 9])
# findZeroSum([12, 34, -46])
# findZeroSum([0, 0, 0])
# findZeroSum([-2, 2, 0, -2, 2])


def findZeroSum(arr):
    n = len(arr)
    results = set()

    arr.sort()
    if n < 3:
        return []
    for i in range(n - 2):
        j = i+1
        k = n-1
        while j < k:
            if arr[i]+arr[j]+arr[k] == 0:
                results.add((arr[i],arr[j],arr[k]))
                j+=1
                k-=1
            elif arr[i]+arr[j]+arr[k] < 0:
                j+=1
            else:
                k-=1
    return list(results)

if __name__ == "__main__":
    f = sys.stdout

    arr_size = int(input())

    arr = []
    for _ in range(arr_size):
        arr_item = int(input())
        arr.append(arr_item)

    res = findZeroSum(arr)

    f.write("\n".join(res))
    f.write('\n')
    f.close()

print(findZeroSum([10, 3, -4, 1, -6, 9]))
print(findZeroSum([12, 34, -46]))
print(findZeroSum([0, 0, 0]))
print(findZeroSum([-2, 2, 0, -2, 2]))



'''
=== EDITORIAL ===
Brute force solution
A simple solution is to use three nested loop and check for each possible combination if their sum is zero. 
To avoid duplicate answers, we need to hash the triplet and store it in a set. An easy way to hash the triplet is 
by converting them to string.

Example: ‘-1,1,0’

Extra space needed will be the number of unique triplets that contribute to the answer.

Space Complexity: O(n^3)
Time Complexity: O(n^3)

Optimal solution
Optimal solution will use the two pointer method. In a two pointer method, we maintain a left and a right pointer 
to the sorted array. If the sum is more than intended, we decrease the right pointer. Otherwise, we increase the left 
pointer. Two pointer works in linear time complexity.



First, we will sort the array. Then, for every index, we will apply two pointer technique to find the sum -arr[index].
We will then add unique triplets to the answer.

Space Complexity: O(n^3)
Time Complexity: O(n^2 + nlog(n))

def findZeroSum(nums, k=0):
    if not nums or len(nums) < 3:
        return []
    n = len(nums)
    output = []
    nums.sort()
    for i, num in enumerate(nums[:-2]):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l = i + 1
        r = n - 1
        while l < r:
            s = num + nums[l] + nums[r]
            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                output.append([num, nums[l], nums[r]])
                # remove duplicates
                while l + 1 < r and nums[l] == nums[l + 1]:
                    l += 1
                while r - 1 > l and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1

    # return output
    #  hackerrank wants a string output :-/ ugh
    return map(lambda x: ','.join([str(a) for a in x]), output)


n = [6, 10, 3, -4, 1, -6, 9]
print findZeroSum(n)
n = [6, -1, -1, 0, 0, 1, 1]
print findZeroSum(n)
'''
