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
