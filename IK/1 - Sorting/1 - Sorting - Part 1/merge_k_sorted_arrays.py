import os
import sys
import heapq
'''
Problem Statement:
This is a popular facebook problem. Given K sorted arrays of size N each, merge them and print the sorted output.
Assume N is very large compared to K. N may not even be known. The arrays could be just sorted streams, for instance,
timestamp streams.

All arrays might be sorted in increasing manner or decreasing manner. Sort all of them in the manner they appear.

* Don't use inbuilt sorts or any standard sorting algorithm after simply merging the lists. *

Note:
Repeats are allowed.
Negative numbers and zeros are allowed.
Assume all arrays are sorted in the same order. Preserve that sort order in output.
It is possible to find out the sort order from at least one of the arrays.

Input Format:
2-D Integer array
Repeats possible
Individual integer array is sorted

Output Format:
Return an integer array containing all elements from all individual arrays combined.

Constraints:
2 <= N <= 500
1 <= K <= 500
-10^6 <= element <= 10^6

Sample Test Case:
Sample Input-1:
K = 3, N =  4
arr[][] = { {1, 3, 5, 7},
            {2, 4, 6, 8},
            {0, 9, 10, 11}} ;

Sample Output-1:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
'''

def merge_k_sorted_lists(list_of_lists):
    merged_list = []
    heap = []
    i = 0
    while i < len(list_of_lists):
        if len(list_of_lists[i]) > 0:
            heapq.heappush(heap, (list_of_lists[i][0],i))
            del list_of_lists[i][0]
            i+=1
        else:
            del list_of_lists[i]

    while len(heap) > 0:
        value,list_index = heapq.heappop(heap)
        merged_list.append(value)
        if len(list_of_lists[list_index]) > 0:
            heapq.heappush(heap,(list_of_lists[list_index][0], list_index))
            del list_of_lists[list_index][0]

    return merged_list

if __name__ == "__main__":
    f = sys.stdout

    arr_rows = int(input())
    arr_columns = int(input())

    arr = []

    for _ in range(arr_rows):
        arr.append(list(map(int, input().rstrip().split())))

    res = merge_k_sorted_lists(arr)

    f.write('\n'.join(map(str, res)))
    f.write('\n')

    f.close()

print(merge_k_sorted_lists([[0,0,3],[3,3,4],[2,22,3000]]))
# print(merge_k_sorted_lists([[0,3],[3,3,4],[2,22,3000]]))
# print(merge_k_sorted_lists([[],[3,3,4],[2,22,3000]]))
# print(merge_k_sorted_lists([[],[],[]]))
# print(merge_k_sorted_lists([[3],[2],[1]]))
# print(merge_k_sorted_lists([[3],[2],[1],[3],[2],[1]]))



'''
=== EDITORIAL ===
Editorial:
First step is to check if the input is in increasing sorted manner or in decreasing sorted manner. Let's solve it for 
increasingly sorted input.

A naive approach would be to add all elements to one collection and then sort them out. We can build on our solution 
following the idea of the naive solution. At any given point of time, the smallest element would be from the pool of 
candidate smallest elements formed by adding the elements at start of all arrays. When we remove the smallest element
from the pool, we will add the next element from that array.

We can maintain a min priority queue to carry out these operations. For decreasingly sorted manner, maintain a max 
priority queue.

Time Complexity: O(NK*Log(K))
Space Complexity: O(K + NK)

from heapq import heappush, heappop

def mergeArrays(arrs):
    heap = []
    k = len(arrs)
    n = len(arrs[0])
    output = []

    # put the first elements in the array
    for i in range(k):
        heappush(heap, (arrs[i][0], i, 0))

    for _ in range(k*n):
        curr_min, arr_idx, item_idx = heappop(heap)
        output.append(curr_min)
        next_item_idx = item_idx+1
        if next_item_idx < n:
            heappush(heap, (arrs[arr_idx][next_item_idx], arr_idx, next_item_idx))

    return output


ars = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]
print mergeArrays(ars)

ars2 = [[6, 10, 15], [7, 9, 18]]
print mergeArrays(ars2)

'''
