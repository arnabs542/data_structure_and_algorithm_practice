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
groupNoAdj(0, [2], 2) → true
groupNoAdj(0, [2, 5, 10, 4, 1], 13) → true
groupNoAdj(0, [2, 5, 10, 4, 1], 9) → true
'''
def groupNoAdj(index, arr, target):
    if index >= len(arr):
        return target==0

    if index < 0:
        return False
    using = False

    if arr[index] == target:
        return True
    if arr[index] < target:
        using = groupNoAdj(index+2, arr, target-arr[index])
        if using:
            return True
    return groupNoAdj(index+1, arr, target)

# print(groupNoAdj(0, [2, 5, 10, 4], 12))
# print(groupNoAdj(0, [2, 5, 10, 4], 14))
# print(groupNoAdj(0, [2, 5, 10, 4], 7))
# print(groupNoAdj(0, [2], 2))
# print(groupNoAdj(0, [2, 5, 10, 4, 1], 13))
# print(groupNoAdj(0, [2, 5, 10, 4, 1], 9))

'''
Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given 
target with these additional constraints: all multiples of 5 in the array must be included in the group. If the value 
immediately following a multiple of 5 is 1, it must not be chosen. (No loops needed.)

groupSum5(0, [2, 5, 10, 4], 19) → true
groupSum5(0, [2, 5, 10, 4], 17) → true
groupSum5(0, [2, 5, 10, 4], 12) → false
'''
def groupSum5(index, arr, target):
    if index >= len(arr):
        return target==0
    if index < 0:
        return False

    if arr[index]%5==0:
        if index+1 < len(arr) and arr[index+1]==1:
            return groupSum5(index+2, arr, target-arr[index])
        return groupSum5(index+1, arr, target-arr[index])

    if arr[index] <= target:
        using = groupSum5(index+1, arr, target-arr[index])
        if using:
            return True
    return groupSum5(index+1, arr, target)

# print(groupSum5(0, [2, 5, 10, 4], 19))
# print(groupSum5(0, [2, 5, 10, 4], 17))
# print(groupSum5(0, [2, 5, 10, 4], 12))

'''
Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given 
target, with this additional constraint: if there are numbers in the array that are adjacent and the identical value, 
they must either all be chosen, or none of them chosen. For example, with the array {1, 2, 2, 2, 5, 2}, either all 
three 2's in the middle must be chosen or not, all as a group. (one loop can be used to find the extent of the 
identical values).

groupSumClump(0, [2, 4, 8], 10) → true
groupSumClump(0, [1, 2, 4, 8, 1], 14) → true
groupSumClump(0, [2, 4, 4, 8], 14) → false 
groupSumClump(0, [1, 2, 2, 2, 2, 5, 2], 9) → true 
groupSumClump(0, [1, 2, 2, 2, 2, 5, 2], 8) → true
groupSumClump(0, [9, 2, 2, 2, 2, 5, 2], 6) → false 
'''
def groupSumClump(index, arr, target):
    if index >= len(arr):
        return target==0
    if index < 0:
        return False

    if arr[index]==target:
        return True
    if arr[index] < target:
        i = index+1
        adjacentNumCount = 1
        while i < len(arr) and arr[i]==arr[index]:
            i+=1
            adjacentNumCount+=1
        using = False
        if arr[index]*adjacentNumCount <= target:
            using = groupSumClump(index+adjacentNumCount, arr, target-(arr[index]*adjacentNumCount))
            if using:
                return True
        return groupSumClump(index+adjacentNumCount, arr, target)
    return groupSumClump(index+1, arr, target)

# print(groupSumClump(0, [2, 4, 8], 10))
# print(groupSumClump(0, [1, 2, 4, 8, 1], 14))
# print(groupSumClump(0, [2, 4, 4, 8], 14))
# print(groupSumClump(0, [1, 2, 2, 2, 2, 5, 2], 9))
# print(groupSumClump(0, [1, 2, 2, 2, 2, 5, 2], 8))
# print(groupSumClump(0, [9, 2, 2, 2, 2, 5, 2], 6))


