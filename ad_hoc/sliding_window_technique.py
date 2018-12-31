'''
Given an array of integers of size ‘n’.
Our aim is to calculate the maximum sum of ‘k’
consecutive elements in the array.

Input  : arr[] = {100, 200, 300, 400}
         k = 2
Output : 700

Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}
         k = 4
Output : 39
We get maximum sum by adding subarray {4, 2, 10, 23}
of size 4.

Input  : arr[] = {2, 3}
         k = 3
Output : Invalid
'''

'''
# arr = {1,4,2,3}
# k = 2
sum = 1+4+2 - 1 + 3 - 4 
max = 
'''

def max_sum_of_k(arr, k):
    if k > len(arr):
        raise ValueError

    current_sum = max_sum = sum(arr[0:k])
    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i-k]  #####
        max_sum = max(max_sum, current_sum)

    return max_sum

# print(max_sum_of_k([100,4,1,900,2], 2))


'''
Contiguous Sequence Sums to a Given Integer

Description
Given an array of unsorted integers and a integer target, return true if a contiguous subarray sums up to the integer 
target. Otherwise, return false.

EXAMPLE
arr = [1,4,6,21]
target = 10
TRUE because [4,6] is a subarray that sums to 10

arr = [1,4,6,21]
target = 9
FALSE because there is no subarray that sums to 9
'''

def is_target_in_subarray(arr, target):
    start = end = 0

    total = 0
    while end < len(arr):
        total += arr[end]
        end += 1

        while total > target and start < end -1:
            total -= arr[start]
            start += 1

        if total == target:
            print(arr[start:end])
            return True
    return False

arr = [1,4,6,21]
target = 1
# print(is_target_in_subarray(arr, target))

'''
Description
Find the sum of contiguous subarray within an array of numbers (both positive and negative) which has the largest sum. 
Return an integer representing the largest sum 

EXAMPLES
arr = [-2,4,-1,-2,1,5,-3,-15,2,3]
output = 6 because [4,-1,-2,5] is the largest sum

arr = [1,4,6,21]
output = 32 because the whole array is the largest sum
'''

def largest_sum_in_array(arr):
    current_total = max_sum = 0
    for i in range(len(arr)):
        current_total += arr[i]
        max_sum = max(max_sum, current_total)

        if current_total <= 0:
            current_total = 0

    return max_sum

# arr = [-2,4,-1,-2,1,5,-3,-15,2,3]
# print(largest_sum_in_array(arr))
# arr = [1,4,6,21]
# print(largest_sum_in_array(arr))

'''
Description
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in 
complexity O(n). Return the string that represents this minimum window that contains “ABC”

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"  # "BANC" is the smallest window in S that contains all character in T

Input: S = "ADABDCEBANAC", T = "AABC"
Output: = "BANAC" # "BANAC" is the smallest window in S that contains all character in T. This substring must contain 
two A's
'''

def minWindowSubstring(S, T):
    S = list(S)
    T = list(T)
    shortest = [0, float('inf')]
    requiredCounts = dict()
    windowCounts = dict()

    missingCharacters = len(set(T))

    for i in range(len(T)):
        if T[i] in requiredCounts:
            requiredCounts[T[i]] += 1
        else:
            requiredCounts[T[i]] = 1

    for i in range(len(T)):
        windowCounts[T[i]] = 0

    slow = 0
    for fast in range(len(S)):
        if S[fast] in windowCounts:
            windowCounts[S[fast]] += 1
            if windowCounts[S[fast]] == requiredCounts[S[fast]]:
                missingCharacters -= 1

        while missingCharacters == 0:
            if fast-slow < shortest[1]-shortest[0]:
                shortest[0] = slow
                shortest[1] = fast

            if S[slow] in windowCounts:
                windowCounts[S[slow]] -= 1
                if windowCounts[S[slow]] < requiredCounts[S[slow]]:
                    missingCharacters += 1

            slow += 1

    if shortest[1] == float('inf'):
        return "No Substring"

    return ''.join(S[shortest[0]: shortest[1]+1])

print(minWindowSubstring('ADCABDCE', 'ABC'))
print(minWindowSubstring('ADABDCEBANAC', 'AABC'))
