from copy import deepcopy
'''
Davis has a number of staircases in his house and he likes to climb each staircase 1, 2, or 3 steps at a time. Being a
very precocious child, he wonders how many ways there are to reach the top of the staircase.

Given the respective heights for each of the  staircases in his house, find and print the number of ways he can climb
each staircase, module 10^9+7 on a new line.

For example, there is s=1 staircase in the house that is n=5 steps high. Davis can step on the following sequences of
steps:

1 1 1 1 1
1 1 1 2
1 1 2 1
1 2 1 1
2 1 1 1
1 2 2
2 2 1
2 1 2
1 1 3
1 3 1
3 1 1
2 3
3 2

There are 13 possible ways he can take these 5 steps.

Example Inputs:
1
3
7

Expected Outputs:
1
4
44
'''

def stairs_rec_print(soFar, n):
    if n < 0:
        return
    if n == 0:
        print(soFar)
    else:
        next = deepcopy(soFar)
        for i in range(1,4):
            next.append(i)
            stairs_rec_print(next, n-i)
            next.pop()


# memo[1] = 1
# memo[2] = 2
# memo[4] = 2

def stairs_rec(n, memo=None):
    if memo == None:
        memo = dict()
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    else:
        count = 0
        for i in range(1,4):
            if n-i >= 0:
                count += stairs_rec(n-i, memo)
            else:
                break
        memo[n] = count
        return count

def stairs(n):
    return stairs_rec(n)

print(stairs(100))
