# Given a sorted list of integers and a target integer return True if it exists in the array and False if it doesn't

def binary_search(arr, target):
    if len(arr) == 0:
        return False
    if len(arr) == 1:
        return target == arr[0]

    midpoint_index = len(arr)//2
    midpoint_element = arr[midpoint_index]

    if midpoint_element == target:
        return True
    if midpoint_element < target:
        return binary_search(arr[midpoint_index:], target)
    if midpoint_element > target:
        return binary_search(arr[:midpoint_index], target)

# arr = [7, 20, 53, 53, 100, 200, 210]
# print(binary_search(arr, 20))
# print(binary_search(arr, 7))
# print(binary_search(arr, 53))
# print(binary_search(arr, 100))
# print(binary_search(arr, 200))
# print(binary_search(arr, 210))
# print(binary_search(arr, 5))
# print(binary_search(arr, 54))
# print(binary_search(arr, 52))

def binary_search_using_indices(arr, target, index_start=None, index_end = None):
    if index_start == None or index_end == None:
        index_start = 0
        index_end = len(arr) - 1

    arr_length = (index_end - index_start) + 1

    if index_start > index_end:
        return False
    if arr_length == 1:
        return target == arr[index_start]

    midpoint_index = index_start + ((index_end-index_start)//2)
    midpoint_element = arr[midpoint_index]

    if midpoint_element == target:
        return True
    if midpoint_element < target:
        return binary_search_using_indices(arr, target, midpoint_index+1, index_end)
    if midpoint_element > target:
        return binary_search_using_indices(arr, target, index_start, midpoint_index-1)

arr = [7, 20, 53, 53, 100, 200, 210]
print(binary_search_using_indices(arr, 20))
print(binary_search_using_indices(arr, 7))
print(binary_search_using_indices(arr, 53))
print(binary_search_using_indices(arr, 100))
print(binary_search_using_indices(arr, 200))
print(binary_search_using_indices(arr, 210))
print(binary_search_using_indices(arr, 5))
print(binary_search_using_indices(arr, 54))
print(binary_search_using_indices(arr, 52))
