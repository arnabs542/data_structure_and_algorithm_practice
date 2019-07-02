from copy import deepcopy

'''
Palindromic Decomposition Of A String
Problem Statement:
A palindromic decomposition of string is a decomposition of the string into sub-strings, such that all those 
sub-strings are valid palindromes.

Given a string s, you have to find ALL possible palindromic decompositions of it.

Input Format:
There is only one argument denoting string s.

Output Format:
Return array of string containing ALL possible palindromic decompositions of given string. 
To differentiate sub-strings in the decomposed string add '|' between them. (Look at the sample test cases for 
more clarity.)
You need not to worry about the order of strings in your output array. Like for s = "aa", arrays ["a|a", "aa"] 
and ["aa", "a|a"] both will be accepted. (Also note that string itself is also a sub-string.)
Any string in the returned array should not contain any spaces. e.g. s = "ab" then ["a|b"] is expected, 
["a |b"] or ["a| b"] or ["a | b"] will give wrong answer.

Sample Input:
"abracadabra"

Sample Output:
[

    "a|b|r|a|c|a|d|a|b|r|a",

    "a|b|r|a|c|ada|b|r|a",

    "a|b|r|aca|d|a|b|r|a"

]
'''
import sys
import os

def generate_palindromic_decomposition(string):
    results = []
    generate_palindromic_decomposition_rec(list(string), 0, [], results)
    return results

def generate_palindromic_decomposition_rec(string, index, current, results):
    if index == len(string):
        if is_current_section_palindrome(current):
            results.append(''.join(current))
        return

    current.append(string[index])
    generate_palindromic_decomposition_rec(string, index+1, deepcopy(current), results)

    if is_current_section_palindrome(current):
        current.append('|')
        generate_palindromic_decomposition_rec(string, index+1, deepcopy(current), results)


def is_current_section_palindrome(current_string):
    end = len(current_string)-1
    start = len(current_string) - 1
    while start-1 >= 0 and current_string[start-1] != '|':
        start -= 1
    while start <= end:
        if current_string[start] != current_string[end]:
            return False
        start += 1
        end -= 1
    return True

print(generate_palindromic_decomposition("abracadabra"))
print(len(generate_palindromic_decomposition("eeeeeeeeeeeeeeeeeeee"))) # should be 524288

