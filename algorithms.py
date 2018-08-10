# Buble Sort

def bubble_sort(alist):
    swapped = True

    while swapped:
        swapped = False
        for i, v in enumerate(alist[:-1]):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                swapped = True

    return alist

# print(bubble_sort([3,9,-1,0]))

# Insertion Sort
def insertion_sort(alist):
    for i in range(len(alist)):
        j=i
        while j-1 >= 0 and alist[j] < alist[j-1]:
            alist[j],alist[j-1] = alist[j-1],alist[j]
            j = j-1
    return alist



def merge_sort(alist):
    if len(alist) == 1:
        return alist

    mid = len(alist)//2

    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])

    return merge_two_sorted_lists(left, right)

def merge_two_sorted_lists(left, right):
    sorted = []
    while len(left) != 0 and len(right) != 0:
        if left[0] <= right[0]:
            sorted.append(left[0])
            del left[0]
        else:
            sorted.append(right[0])
            del right[0]

    if len(left) > 0:
        sorted.extend(left)
    else:
        sorted.extend(right)

    return sorted


# alist = [1,3,4,9,-2,10]
blist = [10,9,8,7,6,5,4,4,3,2,1,0,-1,3,-5]

a = [-1, 4, 6, 9, 10, 1942323124]
b = [-7, -5, 15]
print(merge_sort(blist))

# print(insertion_sort(alist))
