import sys
import os
import heapq
'''
Problem Statement:
You are given an array of integers which is analogous to a continuous stream of input. Find K largest elements from a 
given stream of numbers. By definition, we don't know the size of the input stream. Hence produce K largest elements 
seen so far, at any given time. For repeated numbers, return them only once.

If there are less than K unique elements, return all of them.
Note:
Represent input stream as an array. Don't rely on its size.
Feel free to use built-in functions if you need a specific data-structure.

Input Format:
Integer array
Repeats are possible
Input may or may not be sorted

Output Format:
Return an integer array containing K largest elements. If there are less than K unique elements, return all of them. 
If there are duplicates, return only one instance.
Order of output does not matter.

Constraints:
1 <= N <= 10^5
1 <= K <= 10^5

Given array may contain duplicate numbers.
Sample Test Case:
Sample Input-1:
arr = [1, 5, 4, 4, 2]; k = 2

Sample Output-1:
[4, 5]

Sample Input-2:
arr = [1, 5, 1, 5, 1]; k = 3

Sample Output-2:
[5, 1]
'''

'''
[1,5,1,5]
make minHeap
for each element in arr
    if size of heap < k
        add element to heap
    else
        if current element is larger than item at top of minHeap
            pop off minHeap and add current element
            heapify

s = set()
while heap size > 0:
    pop element off of heap and add it to the set

return list(s)
'''

def top_k(arr, k):
    heap = []
    distinct_nums = set()
    for value in arr:
        if value not in distinct_nums:
            if len(heap) < k:
                heapq.heappush(heap, value)
            elif value > heap[0]:
                heapq.heapreplace(heap, value)
            distinct_nums.add(value)
    return list([i for i in heap])

# print(top_k([1,5,4,4,2], 2))
# print(top_k([1,5,1,5,1,5], 2))
# print(top_k([], 2))
# print(top_k([1], 2))
# print(top_k([1,1,1,1,1,1,1], 2))
# print(top_k([1,2,2,4,5,8,0], 4))
print(top_k([7, 6, 1, 9, 9, 1, 6, 8, 1, 6, 2, 3, 10, 10, 7, 3, 6, 4, 5, 4], 6))


if __name__ == "__main__":
    f = sys.stdout

    arr_cnt = 0
    arr_cnt = int(input())
    arr_i = 0
    arr = []
    while arr_i < arr_cnt:
        arr_item = int(input())
        arr.append(arr_item)
        arr_i += 1

    k = int(input())

    res = top_k(arr, k);
    for res_cur in res:
        f.write( str(res_cur) + "\n" )

    f.close()


'''
=== EDITORIAL ===
We need to preserve the order of elements in a sorted manner. If we can do that, we can obtain top K elements. Also, 
if an element is smaller than the last element in top k, then that element can be dropped as we are not deleting 
elements.

We can maintain a balanced BST or a sorted set collection. Keep adding new elements to the sorted set and if the size 
of the tree increases more than k, remove the smallest element.

Time Complexity: O(N*log(K))
Space Complexity: O(K)

from heapq import heappush, heappop


def topK(arr, k):
    heap = []
    if not arr:
        return heap
    # use a set to not have duplicates in the heap
    heap_set = set()
    for item in arr:
        if item in heap_set:
            continue
        if len(heap) < k:
            # push the first k items
            heappush(heap, item)
            heap_set.add(item)
        else:
            # then remove the smallest item and push another item if it's greater than the smallest
            # to maintain the invariant of the largest k being in the heap
            if item > heap[0]:
                out = heappop(heap)
                heap_set.remove(out)
                heappush(heap, item)
                heap_set.add(item)
    # at the end return the largest values uniquely
    return heap


a = [1, 5, 4, 4, 2]
k = 2
print topK(a, k)

a = [1, 5, 1, 5, 1]
k = 2
print topK(a, k)

'''
