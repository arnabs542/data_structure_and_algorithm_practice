# Code the standard insertion sort algorithm

def insertion_sort(arr):
    # Key Insight: let's always keep a part of the array (the left) sorted and
    #               just "insert" elements from the right in sorted order
    for i in range(len(arr)):
        temp = arr[i]
        j = i-1
        while j >= 0 and arr[j] > temp:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            j = j-1
    return arr

def insertion_sort2(arr):
    for i in range(len(arr)):
        temp = arr[i]
        for j in range(i, 0, -1):
            arr[j],arr[j-1] = arr[j-1],arr[j]

arr = [9,8,7,6,5,4,3,2,1]
# arr = [2,3,5,7,9]
# arr = []
# arr = [2,1]
# arr = [2]
print(insertion_sort2(arr))
