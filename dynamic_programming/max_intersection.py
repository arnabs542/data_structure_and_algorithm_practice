'''
Given a list of sets, find the set that should be excluded to maximize the size
of the intersection of the remaining sets
'''

def max_intersection(sets):
    size = len(sets)
    if size <= 1:
        return -1
    left = [set()]*len(sets)
    right = [set()]*len(sets)
    left[0] = sets[0]
    right[0] = sets[len(sets)-1]
    for i in range(1, size):
        left[i] = left[i-1] & sets[i]
        right[i] = right[i-1] & sets[len(sets)-i]
    right.reverse()

    max_intersection_length = max(len(right[0]), len(left[-1]))
    best_ignored_intersection = 0
    if len(left[0]) <= len(right[-1]):
        best_ignored_intersection = 0
    else:
        best_ignored_intersection = len(sets)-1

    for i in range(size):
        temp_intersection = left[i-1] & right[i+1]
        if len(temp_intersection) > max_intersection_length:
            max_intersection_length = len(temp_intersection)
            best_ignored_intersection = i
    return best_ignored_intersection

# left = ['same as set 0', set(1,2,3,4), set(4,2,1), set(4,3,1)]
# right = [set(1,3,4), set(4,3,1), set(1,3,2,4), 'same as set[len(sets)-1]']
sets = [set([1,2,3,4]), set([1,3,2,4]), set([1,3,4]), set([1,3,2,4])]
print(max_intersection(sets))
