'''
# Given an array of sorted integers, rearrange the array so that all the unique integers move to the front of the array
in a sorted fashion and the duplicates end up at the back of the array.
 INPUT = [4,8,8,8,9,10,11,11,12,13]

 OUPUT = [4,8,9,10,11,12,13,8,11,8]

'''

arr = [4, 8, 8, 8, 9, 10, 11, 11, 12, 13]

def sort_array_unique_first(arr):
    last_unique = 0
    i = 1
    while i < len(arr):
        if arr[i] != arr[last_unique]:
            last_unique += 1
            arr[i],arr[last_unique] = arr[last_unique],arr[i]
        elif arr[i] == arr[last_unique]:
            last_dup = i
            while arr[last_dup] == arr[last_unique]:
                last_dup += 1
            last_unique += 1
            arr[last_unique],arr[last_dup] = arr[last_dup],arr[last_unique]
            i = last_dup
        i += 1

    return arr

print(sort_array_unique_first(arr))



