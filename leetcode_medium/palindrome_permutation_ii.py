'''
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no
palindromic permutation could be form.

Example 1:

Input: "aabb"
Output: ["abba", "baab"]
Example 2:

Input: "abc"
Output: []
'''

# initialize set
# check if current word is palindrome and add it to the set if it is
# compute each permutation
#   when permutation finishes check if palindrome, if it is add to set
# return list(perm_set)

def is_palindrome(arr):
    start = 0
    end = len(arr)-1
    while start <= end:   # CHECK THIS!
        if arr[start]==arr[end]:
            start+=1
            end-=1
        else:
            return False
    return True

def make_palindrome_and_add(arr, index, perm_set=None):
    if perm_set == None:
        perm_set = set()

    string_len = len(arr)

    if index == string_len-1:
        if is_palindrome(arr):
            perm_set.add(''.join(arr))
    else:
        for j in range(index, string_len):
            arr[index],arr[j]=arr[j],arr[index]
            make_palindrome_and_add(arr, index+1, perm_set)
            arr[index],arr[j]=arr[j],arr[index]
    return perm_set

def generate_palindromic_permutations(string):
    return list(make_palindrome_and_add(list(string), 0))

print(generate_palindromic_permutations("aabb"))
print(generate_palindromic_permutations("abc"))
