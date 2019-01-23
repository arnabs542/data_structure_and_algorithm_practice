'''
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide
and conquer approach, which is more subtle.
'''


def max_subarray(nums):
    current_largest = largest = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > current_largest + nums[i-1]:
            current_largest = nums[i]
        else:
            current_largest = current_largest + nums[i-1]

        if current_largest > largest:
            largest = current_largest
    return current_largest

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
