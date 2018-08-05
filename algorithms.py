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

# alist = [1,3,4,9,-2,10]
alist = [10,9,8,7,6,5,4,4,3,2,1,0,-1,3,-5]

print(insertion_sort(alist))
