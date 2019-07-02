import unittest
import os
import sys
'''
Nuts and Bolts!
Problem Statement:
A disorganized carpenter has a mixed pile of bolts and nuts and would like to find the corresponding pairs of bolts and
nuts. Each nut matches exactly one bolt and vice versa. By trying to match a bolt and a nut the carpenter can see which
one is bigger, but she cannot compare two bolts or two nuts directly. Can you help the carpenter match the nuts and
bolts quickly?

In other words: You are given a collection of nuts of different size and corresponding bolts. You can choose any nut &
any bolt together, from which you can determine whether the nut is larger than the bolt, smaller than the bolt or
matches the bolt exactly. However, there is no way to compare two nuts together or two bolts together. (i.e. we cannot
sort all nuts or sort all bolts). Write an algorithm to match each bolt to its matching nut.

You can make the following assumptions:
There are equal number of nuts and bolts
A given nut uniquely matches a bolt. i.e. There are no extra unmatched nuts or extra bolts. i.e. every nut has one and
only one matching bolt and vice-versa.
Note: You cannot compare a bolt to a bolt and a nut to a nut. So you cannot use in-built sorts.

Input Format:
You will be given two integer arrays, NUTS[] and BOLTS[] of size N.
There is only one to one mapping between NUTS and BOLTS. So there will be no duplicate elements.

Output Format:
Return a String array of size N with an entry for each pair of Nut and its corresponding Bolt separated by space only
once.

Format: “Nut Bolt”
Order of the output does not matter.

Constraints:
1 <= N <= 10^5
1 <= NUT <= 10^9
1 <= BOLT <= 10^9

Sample Test Case:
Sample Input-1:
NUTS = [4, 32, 5, 7]
BOLTS = [32, 7, 5, 4]


Sample Output-1:
4 4
32 32
5 5
7 7
'''

from random import randint
def partition(arr, start, end, pivot):
    i = j = start
    while i < end:
        if arr[i] < pivot:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
        if arr[i] == pivot:
            arr[i],arr[end]=arr[end],arr[i]
            i-=1
        i+=1
    arr[j],arr[end]=arr[end],arr[j]

    return j


def nuts_and_bolts_quicksort(nuts, bolts, start=None, end=None):
    if start==None:
        start = 0
        end = len(nuts)-1

    if start >= end:
        return
    index = randint(start, end)
    pivot = partition(nuts, start, end, bolts[index])
    partition(bolts, start, end, nuts[pivot])
    nuts_and_bolts_quicksort(nuts, bolts, start, pivot-1)
    nuts_and_bolts_quicksort(nuts, bolts, pivot+1, end)


def solve(nuts, bolts):
    result = []
    nuts_and_bolts_quicksort(nuts, bolts)
    for i in range(len(nuts)):
        result.append('{} {}'.format(nuts[i], bolts[i]))
    return result

if __name__ == "__main__":
    f = sys.stdout

    nuts_count = int(input())

    nuts = []

    for _ in range(nuts_count):
        nuts_item = int(input())
        nuts.append(nuts_item)

    bolts_count = int(input())

    bolts = []

    for _ in range(bolts_count):
        bolts_item = int(input())
        bolts.append(bolts_item)

    res = solve(nuts, bolts)

    f.write('\n'.join(res))
    f.write('\n')

    f.close()


NUTS = [4, 32, 5, 7]
BOLTS = [32, 7, 5, 4]

# NUTS = [10, 8, 6, 4, 2, 0, 1, 3, 5, 7, 9]
# BOLTS = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# NUTS = ['@', '#', '$', '%', '^', '&']
# BOLTS = ['$', '%', '&', '^', '@', '#']

print(solve(NUTS, BOLTS))

class test_nutsBolts(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(solve(), 3)
        print("Passed")


tests = test_nutsBolts()
print("TESTS")





'''
=== EDITORIAL ===
Naive solution:

Start with the first bolt and compare it with each nut until we find a match. In the worst case we require n 
comparisons. Doing this for all bolts gives us O(N^2) complexity.

Optimal solution:
We can use quick sort technique to solve this.
This algorithm first performs a partition by picking a random element of bolts array as pivot, rearrange the array of 
nuts and returns the partition index ‘i’ such that all nuts smaller than nuts[i] are on the left side and all nuts 
greater than nuts[i] are on the right side. Next using the nuts[i] we can partition the array of bolts. Partitioning 
operations can easily be implemented in O(n). This operation also makes nuts and bolts array nicely partitioned. 
Now we apply this partitioning recursively on the left and right sub-array of nuts and bolts.

As we apply partitioning on nuts and bolts both so the total time complexity will be Θ(2*NlogN) = Θ(N*logN) on average.
Space Complexity: O(1)
Time Complexity: O(N*Log(N))

from random import randint
from itertools import starmap


def solve(nuts, bolts):
    def _match_paris(low, high):
        if low >= high:
            return

        # choose a random bolt as partition
        idx = randint(low, high)
        pivot = partition(nuts, low, high, bolts[idx])
        # now partition bolts using the pivot from above
        partition(bolts, low, high, nuts[pivot])

        # recursively partition the rest of the arrays
        _match_paris(low, pivot-1)
        _match_paris(pivot+1, high)

    _match_paris(0, len(nuts)-1)
    # print(nuts)
    # print(bolts)

    # Making it match IK OJ's expected output
    # Can do this instead of using map
    # output = []
    # for i, nut in enumerate(nuts):
    #     output.append('%s %s' % (nut, bolts[i]))
    #
    # return output
    return list(starmap(lambda i, nut: '%s %s' % (nut, bolts[i]), enumerate(nuts)))


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, low, high, pivot):
    # We want to partition in such a way that everything less than the pivot is
    # towards the beginning and everything greater than the pivot is towards the end
    # We maintain 2 areas 0 -> i (less than pivot) and i to end greater than pivot
    # if we get an element less than pivot we swap and extend both areas
    # if we get an element greater than pivot we can just extend the second area
    # if we get an element equal to pivot we move it to the end and then swap back
    # to the right place at the end of the while loop
    i, j = low, low
    while j < high:
        if arr[j] < pivot:
            swap(arr, i, j)
            j += 1
            i += 1
        elif arr[j] == pivot:
            swap(arr, j, high)
        else:
            j += 1

    swap(arr, i, high)
    return i

# ------------------------------------------ STOP ------------------------------------------

# TEST RUN


NUTS = [4, 32, 5, 7]
BOLTS = [32, 7, 5, 4]
print(solve(NUTS, BOLTS))
'''
