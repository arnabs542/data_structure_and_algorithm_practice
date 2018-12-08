# Write a recursive function for generating all permutations of an input string. Return them as a set.
#
# Don't worry about time or space complexity—if we wanted efficiency we'd write an iterative version.
# To start, assume every character in the input string is unique.
# Your function can have loops—it just needs to also be recursive.


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

print(permutations("kite"))
