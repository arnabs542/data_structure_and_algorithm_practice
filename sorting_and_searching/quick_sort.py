# My implementation of the classic quick sort algorithm. Uses just the front element of the array as a pivot leading to
# O(n^2) complexity in the worst case and therefore not a good implementation to copy for production level code. :)

'''
def partition(arr, index_start, index_end):
    pivot = arr[index_start]
    left = index_start
    right = index_end

    while left < right:
        while left <= index_end and arr[left] <= pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right],arr[left]

    arr[index_start] = arr[right]
    arr[right] = pivot

    return right

def quick_sort(arr, index_start = None, index_end = None):
    # identify start/end indexes for the array
    # select front element of array as the pivot
    # increment left pointer until you have something greater than pivot
    # increment right pointer until you have something less than the pivot
    #   Note: skip over pivot when evaluating left/right options to switch and stop when left/right pointers meet
    if index_end == None and index_start == None:
        index_start = 0
        index_end = len(arr)-1

    if (index_end > index_start):
        pivot = partition(arr, index_start, index_end)
        quick_sort(arr, index_start, pivot-1)
        quick_sort(arr, pivot+1, index_end)

arr = [9,8,7,6,5,4,3,2,1,-100,-500]
# arr = [15,3,2,1,5,9,7,8,6]
# arr = [55,23,26,2,18,78,23,8,2,3]
quick_sort(arr)
print(arr)
'''

def choosePivot(arr, start, end):
    pass

def partition(arr, start, end, pivot_index):
    # O(n) time
    arr[pivot_index], arr[end] = arr[end],arr[pivot_index]
    pivot = arr[end]

    i = start
    for cur in range(start, end):
        if arr[cur] <= pivot:
            arr[cur],arr[i] = arr[i],arr[cur]
            i+=1

    arr[end],arr[i] = arr[i],arr[end]
    return i

def quicksort(arr, start, end):
    if start == end:
        return arr
    if start > end:
        return
    pivot_index = choosePivot()
    pivot_index = partition(arr, start, end, pivot_index)
    quicksort(arr, start, pivot_index-1)
    quicksort(arr, pivot_index+1, end)


# arr = [9,5,3,1,0,-5,200]
arr = [5,7,9,12,4,8]
# quicksort(arr, 0, len(arr)-1)

partition(arr, 0, len(arr)-1, 2)
