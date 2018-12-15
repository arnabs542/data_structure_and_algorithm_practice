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


def nuts_and_bolts(nuts, bolts):
    result = []
    nuts_and_bolts_quicksort(nuts, bolts)
    for i in range(len(nuts)):
        result.append('{} {}'.format(nuts[i], bolts[i]))
    return result

NUTS = [4, 32, 5, 7]
BOLTS = [32, 7, 5, 4]

# NUTS = [10, 8, 6, 4, 2, 0, 1, 3, 5, 7, 9]
# BOLTS = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# NUTS = ['@', '#', '$', '%', '^', '&']
# BOLTS = ['$', '%', '&', '^', '@', '#']

print(nuts_and_bolts(NUTS, BOLTS))
