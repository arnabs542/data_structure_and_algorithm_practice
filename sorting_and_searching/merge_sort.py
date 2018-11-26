# Code the standard merge sort algorithm

def merge_sort(arr):
    # if length is greater than 1
    # call merge_sort to split it into left and right arrays
    # merge left and right together and return it
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged = merge(left, right)
    return merged

def merge(arr1, arr2):
    merged_arr = []
    while len(arr1) > 0 and len(arr2) > 0:
        if arr1[0] <= arr2[0]:
            merged_arr.append(arr1.pop(0))
        elif arr1[0] > arr2[0]:
            merged_arr.append(arr2.pop(0))

    if len(arr1) > 0:
        merged_arr.extend(arr1)
    elif len(arr2) > 0:
        merged_arr.extend(arr2)
    return merged_arr

# arr = [3,7,9,2,5]
arr = [9,8,7,6,5,4,3,2,1]
# arr = []
# arr = [2,1]
# arr = [2]
print(merge_sort(arr))
