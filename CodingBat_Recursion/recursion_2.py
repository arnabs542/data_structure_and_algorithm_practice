'''

Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given
target? This is a classic backtracking recursion problem. Once you understand the recursive backtracking strategy in
this problem, you can use the same pattern for many problems to search a space of choices. Rather than looking at the
whole array, our convention is to consider the part of the array starting at index start and continuing to the end of
the array. The caller can specify the whole array simply by passing start as 0. No loops are needed -- the recursive
calls progress down the array.

print(groupSum(0, [2, 4, 8], 10) → true
print(groupSum(0, [2, 4, 8], 14) → true
print(groupSum(0, [2, 4, 8], 9) → false
'''
def groupSum(index, arr, target):
    if len(arr) ==0:
        return 0==target
    if index >= len(arr) or index < 0:
        return False

    if arr[index]==target:
        return True

    using_current_index = False

    if arr[index] < target:
        using_current_index = groupSum(index+1, arr, target-arr[index])
        if using_current_index:
            return True

    return groupSum(index+1, arr, target)

# print(groupSum(0, [2, 4, 8], 10))
# print(groupSum(0, [2, 4, 8], 14))
# print(groupSum(0, [2, 4, 8], 9))
# print(groupSum(0, [], 0))
# print(groupSum(0, [], 20))

'''
Given an array of ints, is it possible to choose a group of some of the ints, beginning at the start index, such that 
the group sums to the given target? However, with the additional constraint that all 6's must be chosen. 
(No loops needed.)

groupSum6(0, [5, 6, 2], 8) → true
groupSum6(0, [5, 6, 2], 9) → false
groupSum6(0, [5, 6, 2], 7) → false
groupSum6(0, [8, 6, 2], 8) → true
groupSum6(0, [8, 6, 1], 8) → false
'''
def groupSum6(index, arr, target):
    if len(arr) == 0:
        return 0==target

    if index >= len(arr):
        return target==0

    if index < 0 or target < 0:
        return False

    if arr[index]==6:
        return groupSum6(index+1, arr, target-6)

    using = False
    if arr[index] <= target:
        using = groupSum6(index+1, arr, target-arr[index])
    if using:
        return True

    return groupSum6(index+1, arr, target)

# print(groupSum6(0, [5, 6, 2], 8))
# print(groupSum6(0, [5, 6, 2], 9))
# print(groupSum6(0, [5, 6, 2], 7))
# print(groupSum6(0, [8, 6, 2], 8))
# print(groupSum6(0, [8, 6, 1], 8))

'''
Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given 
target with this additional constraint: If a value in the array is chosen to be in the group, the value immediately 
following it in the array must not be chosen. (No loops needed.)

groupNoAdj(0, [2, 5, 10, 4], 12) → true
groupNoAdj(0, [2, 5, 10, 4], 14) → false
groupNoAdj(0, [2, 5, 10, 4], 7) → false
'''
