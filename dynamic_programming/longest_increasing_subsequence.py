# find the length of the longest increasing subsequence in a given inpu
# e.g. given the sequence [3, 4, -1, 0, 6, 2, 3]
# the length of the longest subsequence is 4 because of [-1 , 0, 2, 3]

def longest_increasing_subsequence_brute_force(a):
    longest = float('-inf')
    for i in range(len(a)):
        count = 1
        j = i
        kept = j
        while j+1 < len(a):
            if a[kept] < a[j+1]:
                count = count + 1
                kept = j+1
            j = j+1
        if longest < count:
            longest = count

    return longest

print(longest_increasing_subsequence_brute_force([3,4,-1,0,6,2,3]))
