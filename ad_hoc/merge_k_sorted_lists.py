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
    i = 0
    for i in range(len(list_of_lists)):
        list = list_of_lists[i]
        if len(list) > 0:
            if list[0]==list[-1]:
                continue
            elif list[0] < list[-1]:
                return merge_k_sorted_lists_min_max(list_of_lists)
            else:
                return merge_k_sorted_lists_min_max(list_of_lists, True)
    return merge_k_sorted_lists_min_max(list_of_lists)


def merge_k_sorted_lists_min_max(list_of_lists, is_max_heap=False):
    merged_list = []
    heap = []
    i = 0
    while i < len(list_of_lists):
        if len(list_of_lists[i]) > 0:
            if is_max_heap:
                heapq.heappush(heap, (-list_of_lists[i][0],i))
            else:
                heapq.heappush(heap, (list_of_lists[i][0],i))
            del list_of_lists[i][0]
            i+=1
        else:
            del list_of_lists[i]

    while len(heap) > 0:
        value,list_index = heapq.heappop(heap)
        if is_max_heap:
            merged_list.append(-value)
        else:
            merged_list.append(value)
        if len(list_of_lists[list_index]) > 0:
            if is_max_heap:
                heapq.heappush(heap,(-list_of_lists[list_index][0], list_index))
            else:
                heapq.heappush(heap,(list_of_lists[list_index][0], list_index))
            del list_of_lists[list_index][0]

    return merged_list


# print(merge_k_sorted_lists([[0,0,3],[3,3,4],[2,22,3000]]))
# print(merge_k_sorted_lists([[0,3],[3,3,4],[2,22,3000]]))
# print(merge_k_sorted_lists([[],[3,3,4],[2,22,3000]]))
# print(merge_k_sorted_lists([[],[],[]]))
# print(merge_k_sorted_lists([[3],[2],[1]]))
# print(merge_k_sorted_lists([[3],[2],[1],[3],[2],[1]]))
# print(merge_k_sorted_lists([[3,0,0],[4,3,3],[3000,22,2]]))
