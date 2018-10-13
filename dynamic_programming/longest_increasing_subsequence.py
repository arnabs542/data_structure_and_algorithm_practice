# find the length of the longest increasing subsequence in a given inpu
# e.g. given the sequence [3, 4, -1, 0, 6, 2, 3]
# the length of the longest subsequence is 4 because of [-1 , 0, 2, 3]

def longest_increasing_subsequence_brute_force(a):
    longest = float('-inf')

    for num in a:


def longest_increasing_subsequence_brute_force_rec(list, position):
    if position > len(list)-1:
        return 0
    best = float('-inf')
    for pos in range(position+1, len(list)-1):
        if list[position] < list[pos]:
            return 1 + longest_increasing_subsequence_brute_force_rec(list, position+1)
    return 0

print(longest_increasing_subsequence_brute_force([3,4,-1,0,6,2,3]))
