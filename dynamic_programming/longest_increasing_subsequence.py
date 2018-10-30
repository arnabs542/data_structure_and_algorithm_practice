# find the length of the longest increasing subsequence in a given string
# e.g. given the sequence [3, 4, -1, 0, 6, 2, 3]
# the length of the longest subsequence is 4 because of [-1 , 0, 2, 3]

def longest_increasing_subsequence(arr):
    current_longest = [1]*len(arr)

    i = 1
    while i < len(arr):
        j=0
        while j < i:
            if arr[j] < arr[i]:
                current_longest[i] = max(current_longest[i], current_longest[j]+1)
            j+=1
        i+=1

    longest = 0

    for length in current_longest:
        if length > longest:
            longest = length
    return longest


print(longest_increasing_subsequence([3,4,-1,0,6,2,3]))
