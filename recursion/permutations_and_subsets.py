from copy import deepcopy
# Write a recursive function for generating all permutations of an input string. Return them as a set.
#
# Don't worry about time or space complexity—if we wanted efficiency we'd write an iterative version.
# To start, assume every character in the input string is unique.
# Your function can have loops—it just needs to also be recursive.

# InterviewKickstart way using no extra space and just passing index around
def permute(arr, i):
    n = len(arr)

    if i==n-1:
        print(arr)
        return
    for j in range(i, n):
        arr[i],arr[j]=arr[j],arr[i]
        permute(arr, i+1)
        arr[i],arr[j]=arr[j],arr[i]

# permute(list("kite"), 0)

# InterviewCake way that's confusing, space-inefficient, and more complex than necessary
def get_permutations(string):
    if len(string) <=1:
        return set([string])

    permutations = set()
    remainingLetters = string[:-1]
    lastLetter = string[-1]
    allPermutationsExceptLastLetter = get_permutations(remainingLetters)
    
    for perm in allPermutationsExceptLastLetter:
        for position in range(len(allPermutationsExceptLastLetter) + 1):
            permutation = perm[:position] + lastLetter + perm[position:]
            permutations.add(permutation)
    return permutations

# print(get_permutations("kite"))

# Stanford lecture way of doing permutations
def permutations_rec(soFar, rest, perms=None):
    if perms == None:
        perms = set()

    if len(rest) <= 0:
        # print(soFar)
        perms.add(soFar)
    else:
        for i in range(len(rest)):
            next = soFar + rest[i]
            remaining = rest[:i] + rest[i+1:]
            permutations_rec(next, remaining, perms)
    return perms

def permutations(string):
    return permutations_rec("", string)

# print(permutations("kite"))


'''
Assume that the input is an array of size 'n' where 'n' is an even number. Additionally, assume that  half the integers
are even and the other half are odd. Print only those permutations where odd and even integers alternate, starting with
odd.
'''
def is_alternating_even_odd_with_odd_start(arr):
    i = 0
    while i < len(arr):
        num = arr[i]
        if i%2==0:
            if num%2==0:
                return False
        else:
            if num%2!=0:
                return False
        i+=1
    return True

def print_alternating_permutations_starting_odd(arr, i = 0):
    if i==len(arr)-1 and is_alternating_even_odd_with_odd_start(arr):
        print(arr)
    for j in range(i, len(arr)):
        arr[i],arr[j]=arr[j],arr[i]
        print_alternating_permutations_starting_odd(arr, i+1)
        arr[i],arr[j]=arr[j],arr[i]

# print_alternating_permutations_starting_odd([2,1,3,9,8])

# Stanford lecture way of doing subsets
def subsets(soFar, rest):
    if len(rest)==0:
        print(soFar)
    else:
        # try using the element
        subsets(soFar + rest[0], rest[1:])
        # try NOT using the element
        subsets(soFar, rest[1:])

# print(subsets("", "kite"))

# subsets('','tdco')

'''
Given an array of positive integers, print only those subsets that have a certain sum. (If the values can be negative,
this is a simple change in the base case, where you print the said subset only if it has the right sum)
'''

def subsets_of_certain_sum(soFar, rest, target):
    if len(rest) == 0:
        if sum(soFar) == target:
            print(soFar)
        return
    consider = rest[0]
    newRest = deepcopy(rest)
    del newRest[0]
    newSoFar = deepcopy(soFar)
    subsets_of_certain_sum(soFar, newRest, target)
    newSoFar.append(consider)
    subsets_of_certain_sum(newSoFar, newRest, target)

subsets_of_certain_sum([], [1,2,45,6,7,3], 10)




























