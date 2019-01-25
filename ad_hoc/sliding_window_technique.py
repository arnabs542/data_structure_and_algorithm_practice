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

# print(minWindowSubstring('ADCABDCE', 'ABC'))
# print(minWindowSubstring('ADABDCEBANAC', 'AABC'))

'''
Given a binary array and an integer m, find the position of zeroes flipping which 
creates maximum number of consecutive 1’s in array.

Input:   arr[] = {1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1}
         m = 2
Output:  5 7
We are allowed to flip maximum 2 zeroes. If we flip
arr[5] and arr[7], we get 8 consecutive 1's which is
maximum possible under given constraints 

Input:   arr[] = {1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1}
         m = 1
Output:  7
We are allowed to flip maximum 1 zero. If we flip 
arr[7], we get 5 consecutive 1's which is maximum 
possible under given constraints.

Input:   arr[] = {0, 0, 0, 1}
         m = 4
Output:  0 1 2
Since m is more than number of zeroes, we can flip
all zeroes.
                  0  1  2  3  4  5  6  7  8  9  10
Input:   arr[] = {1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1}
                           lu
                                                c
                                                
                  0  1  2  3                        
Input:   arr[] = {0, 0, 0, 1}
                  lu
                          c
zeros_we_can_flip = 1
cur_max_zeros = 4
max_zeros = 4
zeros_to_flip = [1,1,1,0]

loop through array end we reach the end
    if current num is a one
        cur_max_zeros += 1
    else:
        if zeros_we_can_flip > 0:
            zeros_we_can_flip -= 1
            cur_max_zeros += 1
            zeros_to_flip[current_index] = 1
        else: # you're on a 0 but there are no more zeros you can flip
            # increase lu until you have zeros_we_can_flip > 0 then continue algorithm
            while last_used < cur_index and zeros_we_can_flip == 0:
                if arr[last_used_index] == 0:
                    zeros_we_can_flip += 1
                    zeros_to_flip[last_used_index] = 0
                    i -= 1
                cur_max -= 1
                last_used += 1
                
            last_used_index += 1 ????? incrementing here will screw up during second while loop?
            
    i += 1
    if max_zeros < cur_max_zeros:
        max_zeros = cur_max_zeros
        
for index,bit in enumerate(zeros_to_flip):
    if bit == 1:
        print(index, end=' ')
'''

def bit_position_for_max_ones(arr, m):
   cur_index = 0
   last_used_index = 0
   cur_max_zeros = 0
   max_zeros = 0
   zeros_we_can_flip = m
   zeros_to_flip = [0]*len(arr)
   while cur_index < len(arr):
       if arr[cur_index] == 1:
           cur_max_zeros += 1
       elif zeros_we_can_flip > 0: # you're on a 0 and you can turn it into a 1
           zeros_we_can_flip -= 1
           cur_max_zeros += 1
           zeros_to_flip[cur_index] = 1
       else: # you're on a 0 and you can't turn it into a one
           while last_used_index <= cur_index and zeros_we_can_flip == 0:
               if arr[last_used_index] == 0 and m != 0:
                   zeros_we_can_flip += 1
                   zeros_to_flip[last_used_index] = 0
                   cur_index -= 1
               cur_max_zeros -= 1
               last_used_index += 1

       max_zeros = max(max_zeros, cur_max_zeros)
       cur_index += 1

   for index,bit in enumerate(zeros_to_flip):
        if bit == 1:
            print(index, end=' ')

# bit_position_for_max_ones([0,0,0,1], 4)
# bit_position_for_max_ones([0,0,0,0], 4)
# bit_position_for_max_ones([0,0,0,0], 1)
# bit_position_for_max_ones([0,0,0,0], 0)
# bit_position_for_max_ones([1,0,0,1,1,0,1,0,1,1,1], 2)
# bit_position_for_max_ones([1,0,0,1,1,0,1,0,1,1,1], 1)
